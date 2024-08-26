import subprocess
import re

# Git 커밋 로그 가져오기
def get_git_log():
    result = subprocess.run(['git', 'log', '--pretty=format:%h %ad %s', '--date=short', '--name-only'], capture_output=True, text=True)
    return result.stdout.strip().split('\n')

# HTML 템플릿 생성
def create_html_template(log_lines):
    html_content = '<!DOCTYPE html>\n<html lang="en">\n<head>\n    <meta charset="UTF-8">\n    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n    <title>Change Log</title>\n</head>\n<body>\n    <h1>Change Log</h1>\n    <ul>\n'
    
    commit_hash = None
    date = None
    message = None
    
    for line in log_lines:
        if line.startswith(' '):  # 파일 경로는 커밋 메시지 후에 나옵니다.
            # 파일 경로
            html_content += f'        <li>{message}, {line.strip()}, {date}</li>\n'
        else:
            # 커밋 로그
            commit_info = re.match(r'([a-f0-9]+) (\d{4}-\d{2}-\d{2}) (.+)', line)
            if commit_info:
                commit_hash, date, message = commit_info.groups()

    html_content += '    </ul>\n</body>\n</html>'
    
    return html_content

# 실행
log_lines = get_git_log()
html_template = create_html_template(log_lines)

# 결과를 파일로 저장
with open('change_log.html', 'w') as file:
    file.write(html_template)

print("HTML 템플릿이 생성되었습니다.")
