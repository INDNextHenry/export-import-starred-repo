# export-import-starred-repo
A simple Python script to accomplish these two tasks: export your Starred Repositories on GitHub (Starred Repositories) and import Starred to your GitHub account.
A temporary file will be created starred_repos.json.

## Usage

***Export:***

```bash
python github_stars.py --action export --token YOUR_GITHUB_TOKEN --username YOUR_USERNAME
```

***Import:***

```bash
python github_stars.py --action import --token YOUR_GITHUB_TOKEN --username YOUR_USERNAME
```
