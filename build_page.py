def main():
    # 个人信息配置
    personal_info = {
        "name": "张三",
        "title": "AI Engineer",
        "description": "AI Engineer passionate about MLOps and automation.",
        "skills": ["Python", "TensorFlow", "Git", "CI/CD", "Docker"],
        "projects": [
            {"name": "项目一", "url": "https://github.com/yourusername/project1"},
            {"name": "项目二", "url": "https://github.com/yourusername/project2"}
        ],
        "contact": {
            "github": "https://github.com/yourusername",
            "linkedin": "https://linkedin.com/in/yourprofile"
        }
    }

    # 构建技能标签
    skills_html = "\n".join(f'<span class="skill">{skill}</span>' for skill in personal_info['skills'])

    # 构建项目链接
    projects_html = "\n".join(f'<li><a href="{project["url"]}" target="_blank">{project["name"]}</a></li>' for project in personal_info['projects'])

    # HTML模板
    html_content = f"""
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{personal_info['name']} - Tech Card</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            line-height: 1.6;
            background-color: #f4f4f4;
        }}
        .container {{
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }}
        h1 {{
            color: #333;
            text-align: center;
            margin-bottom: 10px;
        }}
        .title {{
            text-align: center;
            color: #666;
            font-size: 1.2em;
            margin-bottom: 20px;
        }}
        .skills {{
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            margin: 20px 0;
        }}
        .skill {{
            background: #007bff;
            color: white;
            padding: 5px 15px;
            border-radius: 20px;
            font-size: 0.9em;
        }}
        .projects, .contact {{
            margin: 20px 0;
        }}
        a {{
            color: #007bff;
            text-decoration: none;
        }}
        a:hover {{
            text-decoration: underline;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>{personal_info['name']}</h1>
        <div class="title">{personal_info['title']}</div>
        <p>{personal_info['description']}</p>
        <h2>技能</h2>
        <div class="skills">
            {skills_html}
        </div>
        <h2>项目经历</h2>
        <div class="projects">
            <ul>
                {projects_html}
            </ul>
        </div>
        <h2>联系方式</h2>
        <div class="contact">
            <p>
                <a href="{personal_info['contact']['github']}" target="_blank">GitHub</a> |
                <a href="{personal_info['contact']['linkedin']}" target="_blank">LinkedIn</a>
            </p>
        </div>
    </div>
</body>
</html>
"""


    # 写入文件,用with方法可以代替try-catch-finally

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_content.strip())
    print("index.html generated successfully!")

if __name__ == "__main__":
    main()