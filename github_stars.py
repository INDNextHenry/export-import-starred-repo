import requests
import json
import argparse

# 解析命令行参数
parser = argparse.ArgumentParser(description='Export or Import GitHub Starred Repositories.')
parser.add_argument('--action', choices=['export', 'import'], required=True, help='Action to perform: export or import')
parser.add_argument('--token', required=True, help='GitHub Personal Access Token')
parser.add_argument('--username', required=True, help='GitHub Username')
args = parser.parse_args()

# 设置基本信息
token = args.token
username = args.username
headers = {
    'Authorization': f'token {token}',
    'Accept': 'application/vnd.github.v3+json',
}

def export_starred_repos():
    url = f'https://api.github.com/users/{username}/starred'
    starred_repos_count = 0  # 初始化计数器
    with open('starred_repos.json', 'w') as file:
        file.write('[')  # 开始写入一个JSON数组
        first_repo = True
        while url:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                repos = response.json()
                for repo in repos:
                    if not first_repo:
                        file.write(',')
                    else:
                        first_repo = False
                    json.dump(repo, file, indent=4)  # 写入单个仓库的JSON数据
                    print(repo['full_name'])  # 打印仓库名
                    starred_repos_count += 1  # 增加计数器
                if 'next' in response.links:
                    url = response.links['next']['url']
                else:
                    break
            else:
                print("Failed to fetch starred repositories.")
                break
        file.write(']')  # 结束JSON数组
    print(f"Total starred repositories: {starred_repos_count}")
    print("Starred repositories have been exported.")

def import_starred_repos():
    with open('starred_repos.json', 'r') as file:
        repos = json.load(file)
    print(f"Importing {len(repos)} repositories...")
    for repo in repos:
        repo_full_name = repo['full_name']
        url = f'https://api.github.com/user/starred/{repo_full_name}'
        response = requests.put(url, headers=headers)
        if response.status_code == 204:
            print(f"Starred {repo_full_name}")
        else:
            print(f"Failed to star {repo_full_name}")

if args.action == 'export':
    export_starred_repos()
elif args.action == 'import':
    import_starred_repos()

