import subprocess
import re

# Git 커밋 로그 가져오기
def get_git_log():
    result = subprocess.run(['git', 'log', '--pretty=format:"%h %ad %s"', '--date=short', '--name-only'], capture_output=True, text=True)
    return result.stdout.strip().split('\n')

# HTML 템플릿 생성
def create_html_template(log_lines):
    html_content = '<li class="ready off">\n      My page\n      <ul>\n'
    
    commit_hash = None
    for line in log_lines:
        if line.startswith('"'):
            # 커밋 로그
            commit_info = re.match(r'"([a-f0-9]+) (\d{4}-\d{2}-\d{2}) (.+)"', line)
            if commit_info:
                commit_hash, date, message = commit_info.groups()
        elif line:
            # 파일 경로
            html_content += f'        <li>{message},{line},{date}</li>\n'

    html_content += '      </ul>\n    </li>'
    
    return html_content

# 실행
log_lines = get_git_log()
html_template = create_html_template(log_lines)

# 결과를 파일로 저장
with open('change_log.html', 'w') as file:
    file.write(html_template)

print("HTML 템플릿이 생성되었습니다.")
