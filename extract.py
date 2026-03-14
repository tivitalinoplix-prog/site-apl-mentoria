import json

text = open(r'C:\Users\tivit\.gemini\antigravity\brain\eb784e6e-f6a2-4021-a261-373b104483d4\.system_generated\steps\864\output.txt', 'r', encoding='utf-8').read()

start = text.find('"')
end = text.rfind('"\n')
if start != -1 and end > start:
    json_str = text[start:end+1]
    try:
        html = json.loads(json_str) 
        with open(r'C:\Users\tivit\OneDrive\Desktop\ia-na-veia-site\aura_template.html', 'w', encoding='utf-8') as f:
            f.write(html)
        print("Success!")
    except Exception as e:
        print("Error:", e)
else:
    print("Not found")
