from dns import DNS, Record
import sys

def main():
    ts = []
    with open("PROJ2-DNSTS1.txt","r") as f:
        for line in f.readlines():
            line = line.strip().split(" ")
            ts.append(Record(*line))

    dns = DNS(ts, int(sys.argv[1]))
    dns.listen()

if __name__ == "__main__":
    main()