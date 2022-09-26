<center><h1>Setting up Obsidian Git with GitHub repos</h1></center>


Let's setup Obsidian to sync with your GitHub repository! This guide assumes you know your way around the GitHub website but it does not require any technical knowledge.

# Getting Started
## Installing Git
First of all, you're going to want to install [**Git**](https://git-scm.com/). You can install this by following the instructions on [Git's download page](https://git-scm.com/downloads).  If you already have Git installed, you can skip this section.

After you've installed Git, let's verify the installation by opening a terminal and typing `git version`.

For me, this outputs `git version 2.28.0.windows.1`. If instead, you receive a message indicating that `git` is not recognized by your system, you have installed **Git** incorrectly.

## Uploading your SSH Key to GitHub
Next, let's upload your SSH key to GitHub. This will allow your system to directly update and read from your vault backed up on GitHub.

GitHub has an excellent guide on how to do this, which you can find [here](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/checking-for-existing-ssh-keys). Go ahead and follow through this guide to set up your SSH key.

## Creating a GitHub repository
Next, let's create your GitHub repository. You can use whatever settings you'd like, but the most important part is how you will clone the repository to your machine. 

Once you've created your repository, you should see a couple of options on your webpage: Set up in Desktop, HTTPS, and SSH. Select **SSH** and copy the URL (e.g. `git@github.com:username/repo.git`).

 Next, create a folder where you'd like your Obsidian vault to be located. Following this, you're going to open a terminal in the folder you created a moment ago. 

In this terminal, you will write the following command. You will keep this terminal open for the next step.

```git
git init -b main
git remote add origin git@github.com:username/repo.git
git push -u origin main
```
 
You should replace `git@github.com:username/repo.git` with the URL you copied earlier.