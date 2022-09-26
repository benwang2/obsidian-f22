<center><h1>Setting up Obsidian Git with GitHub repos</h1></center>


Let's setup Obsidian to sync with your GitHub repository! This guide assumes you know your way around the GitHub website but it does not require any technical knowledge.

# Getting Started
## Installing Git
First of all, you're going to want to install [**Git**](https://git-scm.com/). You can install this by following the instructions on [Git's download page](https://git-scm.com/downloads).  If you already have Git installed, you can skip this section.

After you've installed Git, let's verify the installation by opening a terminal and typing `git version`.

For me, this outputs `git version 2.28.0.windows.1`. If instead, you receive a message indicating that `git` is not recognized by your system, you have installed **Git** incorrectly.

## Uploading your SSH Key to GitHub
Next, let's upload your SSH key to GitHub. This will allow your system to directly update and read from your vault stored online.

GitHub has an excellent guide on how to do this, which you can find [here](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/about-ssh).

However, I'll break it down here because their guide is very verbose and can be confusing without technical knowledge.

### 

## Creating a GitHub repository
Next, let's create your GitHub repository. You can use whatever settings you'd like, but the most important part is how you will clone the repository to your machine.

Once we're viewing the repository page (`https://github.com/<username>/<repository>`), you should see a green button labeled "**Code**". Go ahead and click this button, then from the list of options HTTPS, SSH, and GitHub CLI, we're going to select **SSH**.

