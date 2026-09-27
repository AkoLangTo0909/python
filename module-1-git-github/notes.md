# Module 1 — Git & GitHub

**Student:** Pereda,Chris Euki
**Date:** Sept. 26 2026

---

## What is Git? What is GitHub? (explain like you're teaching a friend who's never used either)

[Write your own explanation here. What problem does Git actually solve? How is GitHub different from Git itself?]

---Git is a tool that help you tracks your files whether when there's changes or return on what it was from the start.
While GitHub is a website where you can store your files and work in there. It also can help you share and collaborate your project.

## Key vocabulary (in your own words)

- repository: is the one that store your files and see the changes after the project you make.
- commit: it was a saved point of the project you make that add a text about the project change's.
- branch: a different copy that can be helpful that you can change your project without changing the main project.
- push / pull: Push is sending the project you make in GitHub while the Pull is bringing the changes from GitHub in your computer.
- pull request: a way to ask to see the project you make and see if there's a changes that need to do that can add to the main project.
- merge conflict: When git finds different changes that same part of the file of a project that need to choose how to combine them.

---
I want to avoid)

[What tripped you up? A confusing error message, committing to the wrong branch, a merge conflict — explain it so a classmate reading this avoids the same mistake.]

--- I got a merge conflict when Git found changes to the same part of a file on two branches. Git couldn’t decide which changes to keep, so I had to open the file, choose or combine the changes, and save it. I thought Git would automatically combine all the changes. Next time, I’ll read the conflict carefully, make sure the final version includes the right changes, and then commit the fix.
## Walking through what I did

[Describe, step by step, a real branch → commit → push → PR you did. Include the actual commands you used.]

```
Create a branch the switch to the branch i created
I made some changes to the project i create
i commited the changes of that branch
I push the branch i created to GitHub
I open the pull request on GitHub
# paste your actual commands here
```git switch chris
   git add .
   git commit -m "done"
   git push -u origin 

---

## A mistake I made (or one 

I forgot to stage a file before committing, so it wasn’t included in the commit. I caught it by checking git status, then staged and committed the missing file.
## How this connects to something else
Version control is like keeping labeled save points. It helps me see what changed and return to an earlier version if I need to.

[Optional: how does version control relate to anything else you've learned or used before?]
