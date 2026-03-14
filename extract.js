const fs = require('fs');
let content = fs.readFileSync('C:/Users/tivit/.gemini/antigravity/brain/eb784e6e-f6a2-4021-a261-373b104483d4/.system_generated/steps/680/output.txt', 'utf-8');
content = content.replace("Execution result:\n", "").trim();
try {
    const parsed = JSON.parse(content);
    fs.writeFileSync('C:/Users/tivit/.gemini/antigravity/brain/eb784e6e-f6a2-4021-a261-373b104483d4/aura_scraped.html', parsed, 'utf-8');
    console.log("Success");
} catch(e) {
    console.error(e);
}
