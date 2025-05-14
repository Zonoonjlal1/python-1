from bs4 import BeautifulSoup

html = '''<div><a class="css-o171kl" href="/saudi/a/Manager-Jobs-in-Egypt">Manager</a> <span>· 5 - 15 Yrs of Exp</span><a class="css-o171kl" href="/saudi/a/IT-Software-Development-Jobs-in-Egypt"> · IT/Software Development</a><a class="css-5x9pm1" href="/saudi/a/AWS-Jobs-in-Egypt"> · AWS</a><a class="css-5x9pm1" href="/saudi/a/Information-Technology-IT-Jobs-in-Egypt"> · Information Technology (IT)</a><a class="css-5x9pm1" href="/saudi/a/Software-Jobs-in-Egypt"> · Software</a><a class="css-5x9pm1" href="/saudi/a/Software-Development-Jobs-in-Egypt"> · Software Development</a><a class="css-5x9pm1" href="/saudi/a/DevOps-Jobs-in-Egypt"> · DevOps</a><a class="css-5x9pm1" href="/saudi/a/Cloud-Jobs-in-Egypt"> · Cloud</a><a class="css-5x9pm1" href="/saudi/a/Lambda-Jobs-in-Egypt"> · Lambda</a><a class="css-5x9pm1" href="/saudi/a/EC2-Jobs-in-Egypt"> · EC2</a><a class="css-5x9pm1" href="/saudi/a/DynamoDB-Jobs-in-Egypt"> · DynamoDB</a></div>'''

soup = BeautifulSoup(html, "html.parser")
skills = soup.find_all("a", class_=["css-o171kl", "css-5x9pm1"])
skill_texts = [skill.text.strip(" ·") for skill in skills]

print(skill_texts)