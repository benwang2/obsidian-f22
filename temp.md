<center><h1>Setting up Obsidian Git with GitHub repos</h1></center>


Let's setup Obsidian to sync with your GitHub repository! This guide assumes you know your way around the GitHub website but it does not require any technical knowledge.

# Getting Started
## Installing Git
First of all, you're going to want to install [**Git**](https://git-scm.com/). You can install this by following the instructions on [Git's download page](https://git-scm.com/downloads).  If you already have Git installed, you can skip this section.

After you've installed Git, let's verify the installation by opening a terminal and typing `git version`.

For me, this outputs `git version 2.28.0.windows.1`. If instead, you receive a message indicating that `git` is not recognized by your system, you have installed **Git** incorrectly.

## Uploading your SSH Key to GitHub
**This step will need to be repeated for each synced device.**

Next, let's upload your SSH key to GitHub. This will allow your system to directly update and read from your vault backed up on GitHub.

GitHub has an excellent guide on how to do this, which you can find [here](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/checking-for-existing-ssh-keys). Go ahead and follow through this guide to set up your SSH key.

## Creating a GitHub repository
Next, let's create your GitHub repository. You can use whatever settings you'd like, but the most important part is how you will clone the repository to your machine. 

## Syncing your folder to the GitHub repository
**This step will need to be repeated for each synced device.**

Once you've created your repository, you should see a couple of options on your webpage: Set up in Desktop, HTTPS, and SSH. Select **SSH** and copy the URL (e.g. `git@github.com:username/repo.git`).

Alternatively, if this is an existing repository, you will click the green button labeled "Code" and select the **SSH** option. Copy that URL.

Open a terminal in the folder where your Obsidian vault is stored. In this terminal, you will write the following command. 

```git
git init -b main
git remote add origin git@github.com:username/repo.git
```
 
You should replace `git@github.com:username/repo.git` with the URL you copied earlier.

In a text editor of your choice, add a file named `.gitignore` to your vault. Then, copy and paste the following content into the file.

```.gitignore
.obsidian/app.json
.obsidian/appearance.json
.obsidian/hotkeys.json
.obsidian/workspace
```

### Manual upload
Still in the same terminal, you're going to run the following commands.

```
git add .
git commit -m "Initial commit"
git push
```

After running these commands, you should see that your GitHub repository has updated with all the files.

## Install Obsidian Git
Finally, you will install [Obsidian Git](obsidian://show-plugin?id=obsidian-git) and follow the instructions given by the plugin. You've completed the set up for this device.