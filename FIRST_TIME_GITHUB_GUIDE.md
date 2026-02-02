# 🎓 Complete Beginner's Guide: Your First GitHub Upload

**This guide assumes you know NOTHING about Git or GitHub - I'll explain everything!**

---

## 📱 What is GitHub?

GitHub is like **Google Drive for code**. It:
- Stores your code online safely
- Shows it professionally (like a portfolio website)
- Lets others see and download your work
- Tracks all changes you make over time
- Makes you look professional to employers/professors

**Your repository URL will look like:** `https://github.com/your-username/chain-of-thought-research`

---

## ⏱️ How Long Will This Take?

**First time:** 10-15 minutes  
**Next time:** 2 minutes (you'll know what to do!)

---

## 🎯 Overview: What You'll Do

Here's the big picture:

```
Step 1: Create GitHub Account (if needed)
   ↓
Step 2: Create Empty Repository on GitHub
   ↓
Step 3: Get "Upload Password" (Personal Access Token)
   ↓
Step 4: Open Terminal
   ↓
Step 5: Tell Git WHERE to upload
   ↓
Step 6: Upload your code!
   ↓
Step 7: View it online! 🎉
```

**All the hard work is already done!** Your code is organized and ready to go. You just need to upload it.

---

# 📖 Step-by-Step Instructions

---

## ✅ Step 1: Create a GitHub Account

**Skip this if you already have a GitHub account!**

### Instructions:

1. Go to: **https://github.com/signup**

2. **Enter your email address**
   - Use your university email or personal email
   - Click "Continue"

3. **Create a password**
   - Make it strong! (At least 15 characters or 8+ with a number and lowercase letter)
   - Click "Continue"

4. **Choose a username**
   - This will be in all your URLs: `github.com/YOUR-USERNAME`
   - Choose something professional (e.g., your name)
   - Examples: `leonardomatthew`, `matthew-research`, `lmatthew`
   - Click "Continue"

5. **Verify you're human**
   - Solve the puzzle they give you

6. **Click "Create account"**

7. **Check your email**
   - GitHub will send you a verification code
   - Enter the code

8. **Skip the survey questions** (or answer them, your choice)

✅ **Done!** You now have a GitHub account.

**Remember your username** - you'll need it later!

---

## 📦 Step 2: Create a New Repository on GitHub

A "repository" (or "repo") is just a **fancy word for a folder** on GitHub where your code lives.

### Instructions:

1. **Make sure you're logged into GitHub**
   - Go to: https://github.com

2. **Look at the TOP RIGHT corner**
   - You'll see your profile picture
   - Next to it is a **+ (plus)** icon

3. **Click the + icon**
   - A dropdown menu appears
   - Click **"New repository"**

4. **Fill in the form:**

   #### Repository name:
   ```
   chain-of-thought-research
   ```
   - This will be in your URL
   - No spaces allowed! Use dashes instead
   - You can change it later if you want

   #### Description (optional but recommended):
   ```
   Research project exploring Chain-of-Thought prompting in Large Language Models
   ```
   - This helps people understand what your project is about

   #### Public or Private?
   - **Public** = Anyone can see it (✅ Recommended for portfolios!)
   - **Private** = Only you can see it (Good for unfinished work)
   
   Choose **Public** to show off your work!

   #### ⚠️ CRITICAL - Don't Check These Boxes:
   - ❌ Do NOT check "Add a README file"
   - ❌ Do NOT check "Add .gitignore"
   - ❌ Do NOT select a license
   
   **Why?** Because you already have these files! If you add them again, GitHub will complain about conflicts.

5. **Click the big green "Create repository" button** at the bottom

6. **You'll see a page with code/instructions**
   - Don't panic! 
   - Ignore the instructions GitHub gives you
   - I'll give you better ones below

7. **Copy your repository URL**
   - You'll see a URL like: `https://github.com/YOUR-USERNAME/chain-of-thought-research.git`
   - Keep this page open (or remember the URL)

✅ **Done!** You created an empty home on GitHub for your code.

---

## 🔑 Step 3: Get Your "Upload Password" (Personal Access Token)

GitHub doesn't let you use your regular password to upload code (for security). You need a special "token" - think of it as a **temporary password just for uploading code**.

### Why Do I Need This?
- Your regular password is for logging into the website
- The token is for uploading code from Terminal
- It's more secure (you can delete tokens without changing your main password)

### Instructions:

1. **Click your profile picture** (top right corner of GitHub)

2. **Click "Settings"**
   - It's near the bottom of the dropdown menu

3. **Scroll down the LEFT sidebar** all the way to the bottom
   - Look for **"Developer settings"**
   - Click it

4. **In the left menu, click "Personal access tokens"**
   - Then click **"Tokens (classic)"**

5. **Click "Generate new token"**
   - Then click **"Generate new token (classic)"**

6. **GitHub might ask for your password**
   - Enter it and click "Confirm"

7. **Fill in the token form:**

   #### Note (Description):
   ```
   Upload Research Code
   ```
   (This is just a reminder for yourself - what you'll use this token for)

   #### Expiration:
   - Choose **90 days** (recommended)
   - Or choose "No expiration" if you want it to last forever
   
   #### Select scopes (Permissions):
   - Find the checkbox next to **"repo"**
   - ✅ Check that box (it will automatically check sub-boxes too)
   - **Don't check anything else!** Just "repo" is enough

8. **Scroll to the bottom**
   - Click the green **"Generate token"** button

9. **⚠️ SUPER IMPORTANT - YOU'LL SEE A LONG GREEN STRING:**
   ```
   ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
   ```
   
   **DO THIS RIGHT NOW:**
   - **Copy this entire string immediately!**
   - **Paste it somewhere safe:**
     - Notes app
     - TextEdit file
     - Password manager
   - **You will NEVER see this token again!**
   - If you lose it, you'll have to create a new one

✅ **Done!** You have your upload password (token). Keep it safe!

**This token IS your password for uploading. Treat it like a password!**

---

## 💻 Step 4: Open Terminal and Navigate to Your Code

"Terminal" is an app on your Mac that lets you type commands. Don't worry - I'll explain every command!

### How to Open Terminal:

**Method 1: Using Spotlight (Easiest)**
1. Press **Command (⌘) + Space** on your keyboard
2. Type: `Terminal`
3. Press **Enter**

**Method 2: Using Finder**
1. Open Finder
2. Go to Applications → Utilities → Terminal
3. Double-click Terminal

**You'll see a window with text** - this is Terminal! It looks scary but it's just a different way to use your computer.

### Navigate to Your Repository Folder:

Now we need to "go into" your Research Tsinghua folder using Terminal.

**Copy this command exactly (don't change anything!):**

```bash
cd "/Users/leonardomatthew/Desktop/Research Tsinghua"
```

**Press Enter**

#### What This Does:
- `cd` = "change directory" (go to a folder)
- The path in quotes = your Research Tsinghua folder
- You're now "inside" your project folder

#### How to Know It Worked:
Your Terminal will show something like:
```
leonardomatthew@MacBook-Air Research Tsinghua %
```

The folder name appears before the `%` symbol!

✅ **Done!** Terminal is now in the right place.

---

## 🔗 Step 5: Connect Your Local Folder to GitHub

Right now, your code is only on your Mac. GitHub exists online but doesn't know about your code yet. This step tells Git: **"When I say 'upload', send my code to THIS specific GitHub address."**

Think of it like writing the destination address on a package before mailing it.

### The Command:

**⚠️ IMPORTANT:** You need to replace `YOUR-USERNAME` with your actual GitHub username!

```bash
git remote add origin https://github.com/YOUR-USERNAME/chain-of-thought-research.git
```

#### Example:
If your GitHub username is `johnsmith`, you would type:
```bash
git remote add origin https://github.com/johnsmith/chain-of-thought-research.git
```

**After typing it, press Enter**

#### What This Does:
- `git remote add` = "Add a destination for uploading"
- `origin` = A nickname meaning "the main destination"
- The URL = The actual address on GitHub

#### What You'll See:
**Nothing!** That's normal. No output means it worked.

### Verify It Worked (Optional but Recommended):

Type this command:
```bash
git remote -v
```

**Press Enter**

You should see:
```
origin  https://github.com/YOUR-USERNAME/chain-of-thought-research.git (fetch)
origin  https://github.com/YOUR-USERNAME/chain-of-thought-research.git (push)
```

If you see this, it worked! ✅

✅ **Done!** Your computer now knows where to send your code.

---

## 🚀 Step 6: Upload Your Code to GitHub!

This is THE moment! Let's send your code to GitHub.

### The Command:

Type this exactly:
```bash
git push -u origin main
```

**Press Enter**

#### What This Does:
- `git push` = "Upload my code"
- `-u origin main` = "To the destination we just set up, on the 'main' branch"

### What Will Happen Next:

#### 1. You'll see text scrolling:
```
Enumerating objects: 28, done.
Counting objects: 100% (28/28), done.
Delta compression using up to 8 threads
Compressing objects: 100% (24/24), done.
```
**This is normal!** Your code is being prepared for upload.

#### 2. Terminal will ask for your username:
```
Username for 'https://github.com':
```

**Type your GitHub username and press Enter**

Example: `leonardomatthew`

#### 3. Terminal will ask for your password:
```
Password for 'https://leonardomatthew@github.com':
```

**⚠️ IMPORTANT:** 
- **DO NOT type your GitHub password!**
- **Paste your Personal Access Token** (the `ghp_xxx...` string you saved earlier)
- **You won't see it as you paste** - this is normal for security!
- **Press Enter**

#### 4. The upload begins!
```
Writing objects: 100% (28/28), 1.2 MiB | 500 KiB/s, done.
Total 28 (delta 2), reused 0 (delta 0)
remote: Resolving deltas: 100% (2/2), done.
```

#### 5. Success message:
```
To https://github.com/YOUR-USERNAME/chain-of-thought-research.git
 * [new branch]      main -> main
Branch 'main' set up to track remote branch 'main' from 'origin'.
```

### 🎉 **YOU DID IT! YOUR CODE IS NOW ON GITHUB!**

✅ **Done!** Your code is successfully uploaded!

---

## 🎊 Step 7: View Your Repository Online

Let's see your work online!

### Instructions:

1. **Open your web browser** (Safari, Chrome, etc.)

2. **Go to:**
   ```
   https://github.com/YOUR-USERNAME/chain-of-thought-research
   ```
   (Replace YOUR-USERNAME with your actual username)

3. **YOU SHOULD SEE:**
   - ✅ Your beautiful README with all the documentation
   - ✅ Three project folders (project1, project2, project3)
   - ✅ All your files and code
   - ✅ Your visualizations (PNG images)
   - ✅ LICENSE, requirements.txt, etc.

4. **Click around!**
   - Click on folders to see what's inside
   - Click on README.md to see it formatted nicely
   - Click on code files to read them

### 🎊 Congratulations! 🎊

**You just uploaded your first GitHub repository!**

You can now:
- ✅ Share this URL with anyone
- ✅ Add it to your resume/CV
- ✅ Post it on LinkedIn
- ✅ Show it to professors or employers
- ✅ Let others download your code

---

# 🆘 Troubleshooting Common Problems

## ❌ Problem: "fatal: remote origin already exists"

**What it means:** You already told Git where to upload.

**Solution:**

Remove the old destination and add it again:
```bash
git remote remove origin
git remote add origin https://github.com/YOUR-USERNAME/chain-of-thought-research.git
```

---

## ❌ Problem: "Authentication failed" or "Invalid username or password"

**What it means:** GitHub didn't accept your credentials.

**Common causes:**
1. You used your GitHub password instead of the token
2. You copied the token incorrectly (with extra spaces)
3. Your token expired

**Solution:**

1. Go back to GitHub
2. Generate a NEW token (follow Step 3 again)
3. Try the `git push` command again
4. When it asks for password, paste the NEW token

---

## ❌ Problem: "Repository not found" or "fatal: repository does not exist"

**What it means:** Git can't find the repository on GitHub.

**Common causes:**
1. You didn't create the repository on GitHub yet (Step 2)
2. Your username is spelled wrong in the URL
3. The repository name doesn't match

**Solution:**

Check the URL:
```bash
git remote -v
```

If it's wrong:
```bash
git remote remove origin
git remote add origin https://github.com/CORRECT-USERNAME/chain-of-thought-research.git
```

---

## ❌ Problem: "Updates were rejected" or "failed to push"

**What it means:** GitHub has changes your computer doesn't know about.

**Solution:**

Pull the changes first, then push:
```bash
git pull origin main --rebase
git push origin main
```

---

## ❌ Problem: Terminal says "command not found: git"

**What it means:** Git isn't installed on your Mac.

**Solution:**

Install Xcode Command Line Tools:
```bash
xcode-select --install
```

Follow the prompts, then try again.

---

## ❌ Problem: I lost my Personal Access Token!

**What it means:** You didn't save the token and now the page is gone.

**Solution:**

No problem! Just create a new one:
1. Go to GitHub → Settings → Developer settings → Personal access tokens
2. Click "Generate new token (classic)"
3. Follow Step 3 again

**You can have multiple tokens!** GitHub doesn't care.

---

## ❌ Problem: The terminal asks for password but nothing appears when I type/paste

**What it means:** This is NORMAL! It's a security feature.

**Solution:**

- Just paste your token (even though you don't see it)
- Press Enter
- It will work!

---

# 📚 Understanding What You Just Did

Let me explain what each step accomplished:

### Step 1: GitHub Account
- You got access to GitHub's platform
- Like creating a Google account to use Google Drive

### Step 2: Create Repository
- You made an empty folder on GitHub
- This is where your code will live online

### Step 3: Personal Access Token
- You got permission to upload code
- Like getting a key card to enter a building

### Step 4: Open Terminal
- You opened the tool that lets you run commands
- Like opening Finder, but using text instead of clicking

### Step 5: Add Remote
- You told Git WHERE on GitHub to send your code
- Like writing an address on a package

### Step 6: Push
- You uploaded all your code to GitHub
- Like clicking "Upload" on Google Drive

### Step 7: View Online
- You confirmed everything worked
- Now your code is online for the world to see!

---

# 🔄 Next Time: Making Updates

After you make changes to your code, here's how to upload the changes:

### Quick Update Process:

```bash
# 1. Go to your folder
cd "/Users/leonardomatthew/Desktop/Research Tsinghua"

# 2. See what changed
git status

# 3. Add all changes
git add .

# 4. Save changes with a message
git commit -m "Describe what you changed"

# 5. Upload to GitHub
git push
```

That's it! Much faster than the first time.

---

# 🎯 Your Repository URL

After uploading, your code lives at:
```
https://github.com/YOUR-USERNAME/chain-of-thought-research
```

**This is YOUR URL! Share it proudly!**

You can:
- Add it to your resume/CV
- Share on LinkedIn: "Excited to share my research on Chain-of-Thought prompting!"
- Email to professors: "Here's the repository for my research project"
- Show in job interviews: "Here's an example of my research work"

---

# 💡 Pro Tips

### 1. Add Topics to Your Repository

Makes it easier for people to find:

1. Go to your repository on GitHub
2. Find "About" section (top right)
3. Click the ⚙️ gear icon
4. Add topics: `machine-learning`, `nlp`, `chain-of-thought`, `llm`, `research`
5. Click "Save changes"

### 2. Pin It to Your Profile

Show it off on your GitHub profile:

1. Go to your GitHub profile
2. Click "Customize your pins"
3. Select your repository
4. Click "Save pins"

### 3. Add a Star ⭐

Bookmark your own repository:

1. Go to your repository
2. Click the "Star" button (top right)
3. Now it's in your starred repositories!

---

# ✅ Checklist: Did Everything Work?

Use this to verify:

- [ ] I created a GitHub account
- [ ] I created a repository on GitHub
- [ ] I generated a Personal Access Token
- [ ] I opened Terminal
- [ ] I ran the `cd` command to navigate to my folder
- [ ] I ran `git remote add origin` to set the destination
- [ ] I ran `git push` to upload
- [ ] I can see my code at `https://github.com/MY-USERNAME/chain-of-thought-research`
- [ ] All my files are there (README, 3 project folders, etc.)
- [ ] The README displays nicely on GitHub

**If you checked all boxes: CONGRATULATIONS! You're done!** 🎉

---

# 🙋 Still Have Questions?

Common questions:

**Q: Can I change the repository name later?**  
A: Yes! Go to Settings in your repository → Change repository name

**Q: Can I make it private later?**  
A: Yes! Go to Settings → Danger Zone → Change visibility

**Q: Can I delete it if I mess up?**  
A: Yes! Go to Settings → Danger Zone → Delete repository (but you won't need to!)

**Q: What if I want to upload a different project?**  
A: Create a new repository on GitHub (Step 2) and repeat the process with a different folder

**Q: Do I need to pay for GitHub?**  
A: No! Public repositories are FREE. Private repositories are also FREE (unlimited).

---

# 🎓 You're Now a GitHub User!

You've learned:
- ✅ How to create a GitHub account
- ✅ How to create a repository
- ✅ How to use Personal Access Tokens
- ✅ Basic Terminal/Git commands
- ✅ How to upload code to GitHub
- ✅ How to share your work online

**This is a valuable skill!** You can now:
- Build a portfolio of projects
- Collaborate with others
- Show your work to employers
- Contribute to open source

---

## 🌟 Next Steps

**Now that you've uploaded your research:**

1. **Share it!**
   - LinkedIn: "Excited to share my research on LLM reasoning!"
   - Twitter: Tag relevant researchers
   - Email: Send to your professor or advisor

2. **Add it to your CV/Resume:**
   ```
   Research Projects:
   - Chain-of-Thought Prompting Research
     https://github.com/YOUR-USERNAME/chain-of-thought-research
   ```

3. **Continue learning:**
   - Try uploading another project
   - Learn more Git commands
   - Explore other people's repositories

---

**Congratulations on uploading your first GitHub repository!** 🎊🎉

You did great! Keep building and sharing your work!

---

*Created for first-time GitHub users | Research Tsinghua Project | 2026*
