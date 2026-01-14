def create_main_page():
    # Personal information configuration
    personal_info = {
        "name": "Deng Chao",
        "title": "AI Engineer",
        "description": "AI Engineer passionate about MLOps and automation.",
        "skills": {
            "Programming Skills": ["Python", "C Language", "C++"],
            "Version Control & DevOps": ["Git", "CI/CD", "Docker"],
            "Technical Skills": ["Data structure", "common algorithm", "software testing"],
            "Communication & Networking": ["3GPP protocols (RRC, S1/X2)", "wireless network Architecture (NSA, SA)", "Wireless signaling process (Attach, Handover,Paging)"],
            "Tools & Software": ["Microsoft Office", "Photoshop", "Photography"]
        },
        "projects": [
            {"time":"2012-2018",  "role": "4G Software Development Engineer",
             "company": "Huawei Technologies Inc, Shenzhen China"
              },
             {"name": "Performance improvement features for Huawei 4G Base Station", 
              "description": "Implemented site-coordination features, convert interference to useful power, site throughput +10%"
              },
            {"name": "Site capacity expansion", 
              "description": "Redesigned resource allocation algorithm and data structure, expand cell capacity from 400 to 1200 users."
              },
            {"name": "Energy Saving", 
              "description": "Developed dynamic power control module, reduce base station energy consumption by 15%",
            },
            {"name": "CPU performance optimization", 
              "description": "Used multiple methods to reduce CPU and memory usage, CPU Usage -20%."},
            {"name": "Software version manager", 
              "description": "Be the leader of critical projects, design version developing plan, coordinate with colleagues to finish project on time."},
           
           
           {"time":"2018-2021", "role": "4G/5G Network Maintenance Engineer",
             "company": "Huawei Technologies Inc, Dongguan China"},
            {"name": "4G Wireless network maintenance", 
              "description": "Be the leader of critical projects, design version developing plan, coordinate with colleagues to finish project on time."},
            {"name": "5G Commercial Launch Support", 
              "description": "Leading critical 5G KPI issue trouble shooting, support massive operators launch 5G on time (Netherlands KPN, Switzerland Sunrise, UK O2 etc.)"},
            {"name": "Software upgrade support", 
              "description": "Support operators software upgrading and led Beta test in Jiangsu."},
          
           {"time":"2021-2024", "role": " Wireless Product Manager",
             "company": "Huawei Morocco, Rabat-Morocco"},
            {"name": "Network insight", 
              "description": "As the Internal technical leader for network insight, responsible for big data analysis through digital platform/Python scripts and provide target network evolution proposal. Organized technical meetings with various level customers and presented as speaker 10+ times."},
            {"name": "Network solution proposal", 
              "description": "Design proper technology and business solution to solve customer concerns and network expansion issues."},
            {"name": "Commercial negotiation", 
              "description": "Lead price negotiation for 10+ projects, total amount to xx M USD."},
            {"name": "Python Learning Demos", "url": "https://github.com/dengchaoccc/HelloWorld7017.git"},
            {"name": "Xu University Training", "url": "https://github.com/dengchaoccc/Xu-Training.git"}
        ],
        "contact": {
            "github": "https://github.com/dengchaoccc",
            "linkedin": "https://linkedin.com/in/yourprofile"
        }
    }

    # 构建技能标签
    skills_html = ""
    for category, skill_list in personal_info['skills'].items():
        skills_html += f'<h3>{category}</h3>\n<div class="skills-category">\n'
        skills_html += "\n".join(f'<span class="skill">{skill}</span>' for skill in skill_list)
        skills_html += '\n</div>\n'

    import re

    def highlight_description(desc):
        # 高亮数字
        desc = re.sub(r'(\d+)', r'<span class="highlight-number">\1</span>', desc)
        # 高亮整个描述
        return f'<mark>{desc}</mark>'

    # 构建项目链接
    projects_html = ""
    for project in personal_info['projects']:
        if 'url' in project:
            projects_html += f'<li><a href="{project["url"]}" target="_blank">{project["name"]}</a></li>\n'
        elif 'name' in project:
            desc = project.get("description", "")
            highlighted_desc = highlight_description(desc)
            projects_html += f'<li><strong>{project["name"]}</strong>: {highlighted_desc}</li>\n'
        elif 'time' in project:
            projects_html += f'<hr>\n<li><strong>{project["time"]} - {project["role"]} at {project["company"]}</strong></li>\n'
        else:
            projects_html += f'<li>{str(project)}</li>\n'

    # HTML模板
    html_content = f"""
<!DOCTYPE html>
<html lang="en">
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
            margin: 20px 0;
        }}
        .skills-category {{
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            margin-bottom: 15px;
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
        .highlight-number {{
            color: #e74c3c;
            font-weight: bold;
        }}
        mark {{
            background-color: #fff3cd;
            padding: 2px 4px;
            border-radius: 3px;
        }}
        hr {{
            border: none;
            height: 2px;
            background-color: #ddd;
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
        <h2>Skills</h2>
        <div class="skills">
            {skills_html}
        </div>
        <h2>Experience & Projects</h2>
        <div class="projects">
            <ul>
                {projects_html}
            </ul>
        </div>
        <h2>Contact Information</h2>
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
    create_main_page()