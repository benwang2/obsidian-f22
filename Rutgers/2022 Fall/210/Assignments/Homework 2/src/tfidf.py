import math
import re

def part1(docs):
    def preproc(docName):
        with open(docName,"r") as f:
            content = f.read()
            content = re.sub("https?:\/\/[^\s]+", "", content) # websites
            content = re.sub("[^A-z0-9_\s]","", content)
            content = re.sub("\s+", " ", content) # extra whitespace

            content = " ".join(word.lower() for word in content.split(" "))

        return content

    def remove_stopwords(content):
        stopwords_file = open("stopwords.txt","r")
        stopwords = {word.strip():True for word in stopwords_file}
        stopwords_file.close()
        return " ".join(word for word in content.split(" ") if word not in stopwords)

    def s_and_l(content):
        rules = ("ing","ly","ment")
        for rule in rules:
            content = re.sub("(\w+)"+rule, r"\1", content)
        return content

    for doc in docs:
        with open("preproc_"+doc.strip(),"w") as f:
            preprocessed = preproc(doc)
            no_stopwords = remove_stopwords(preprocessed)
            root_words = s_and_l(no_stopwords)
            f.write(root_words)

def part2(docs):
    class DocData:
        def __init__(self, name, content):
            terms = content.split(" ") 

            self.freq_map = {word:terms.count(word) for word in set(terms)}
            self.doc_name = name
            self.num_terms = len(terms)

        def get_freq(self, word):
            return self.freq_map[word]

        def get_terms(self):
            return self.freq_map.keys()

        def get_tf(self, word):
            return self.freq_map[word]/self.num_terms

    def compute_tf(doc):
        with open("preproc_"+doc.strip(),"r") as f:
            return DocData(doc, f.read())

    def compute_idf(dataset):
        idf = {}

        terms = set()
        for data in dataset:
            terms.update(data.get_terms())

        for term in terms:
            occ = 0
            for data in dataset:
                if term in data.freq_map:
                    occ += 1
            idf[term] = math.log(len(docs)/occ)+1

        return idf

    dataset: DocData = [compute_tf(doc) for doc in docs]
    idf_scores = compute_idf(dataset)
    
    for data in dataset:
        tf_idf = []
        for term in data.get_terms():
            tf_idf.append((term, data.get_tf(term)*idf_scores[term]))
        
        # make the tf-idf score negative so it's sorted in
        # decreasing order, but still sorting terms alphabetically
        sorted_tfidf = sorted(tf_idf, key=lambda x: (-x[1],x[0]))[:5]
        with open("tfidf_"+data.doc_name,"w") as f:
            f.write("[")
            body = []
            for (term, score) in sorted_tfidf[:5]:
                body.append(f"('{term}', {score:.2f})")
            f.write(", ".join(body))
            f.write("]\n")

def main():
    file = open("tfidf_docs.txt","r")
    docNames = [doc.strip() for doc in file]
    file.close()

    part1(docNames)
    part2(docNames)

    

if __name__ == "__main__":
    main()