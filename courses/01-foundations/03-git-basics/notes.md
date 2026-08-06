# Git Basics

Started: 06 August 2026  
Completed:

## Introduction to Git

### Knowledge Check

#### What kind of program is Git?

Git is a version control system. It tracks changes to files in a project over time and keeps a record of previous versions.

#### What are the differences between Git and a text editor in terms of what they save and their record keeping?

A text editor primarily saves the current version of a file. Git tracks changes across the files and folders in a project and keeps a history of saved versions, allowing you to see how the project has changed over time.

#### Does Git work at a local or remote level?

Git works locally on your computer.

#### Does GitHub work at a local or remote level?

GitHub works remotely by hosting Git repositories online.

#### Why is Git useful for developers?

Git allows developers to see how a project has changed over time. It also makes it possible to inspect or restore previous versions if necessary.

#### Why are Git and GitHub useful for a team of developers?

Git and GitHub allow multiple developers to work locally on the same project while keeping track of their individual contributions. Their changes can be brought together, and conflicts between different changes can be identified and managed.

## Git Basics

### Knowledge Check

#### How do you create a new repository on GitHub?

On the GitHub website, click the `+` button and select **New repository**, then configure and create the repository.

#### How do you copy a repository onto your local machine from GitHub?

Navigate to the directory where you want the repository to be stored, copy the repository's SSH URL from GitHub, and use:

`git clone <SSH-URL>`

This creates a local copy of the repository on your computer.

#### What is the default name of your remote connection?

The default name of the remote connection is `origin`.

#### Explain what `origin` is in `git push origin main`.

`origin` is the name of the remote connection. It identifies the remote repository that the changes will be pushed to.

#### Explain what `main` is in `git push origin main`.

`main` is the name of the branch being pushed. It is the default branch in this repository.

#### Explain the two-stage system that Git uses to save files.

Git uses a two-stage process before changes are saved in its history. First, the desired changes are added to the staging area. The staged changes are then committed to the repository.

#### How do you check the status of your current repository?

Use:

`git status`

This shows the current state of the repository and helps you see which changes have or have not been staged.

#### How do you add files to the staging area in Git?

Use:

`git add .`

This adds the changes in the current directory to the staging area so they can be included in the next commit.

#### How do you commit the files in the staging area and add a descriptive message?

Use:

`git commit -m "message"`

The message should briefly describe the changes included in the commit.

#### How do you push your changes to your repository on GitHub?

Use:

`git push`

This pushes your committed changes to the connected remote repository.

#### How do you look at the history of your previous commits?

Use:

`git log`

This displays the repository's commit history.