from flask import Flask, request, render_template_string, jsonify
import random
import html


app = Flask(__name__)

# Unicode combining marks for the zalgo effect
MARKS_ABOVE = list(map(chr, [
    0x030d, 0x030e, 0x0304, 0x0305, 0x033f, 0x0311, 0x0306, 0x0310, 0x0352, 0x0357,
    0x0351, 0x0307, 0x0308, 0x030a, 0x0342, 0x0343, 0x0344, 0x034a, 0x034b, 0x034c,
    0x0303, 0x0302, 0x030c, 0x0350, 0x0300, 0x0301, 0x030b, 0x030f, 0x0312, 0x0313,
    0x0314, 0x033d, 0x0309, 0x0363, 0x0364, 0x0365, 0x0366, 0x0367, 0x0368, 0x0369,
    0x036a, 0x036b, 0x036c, 0x036d, 0x036e, 0x036f, 0x033e, 0x035b, 0x0346, 0x031a
]))

MARKS_MIDDLE = list(map(chr, [
    0x0315, 0x031b, 0x0340, 0x0341, 0x0358, 0x0321, 0x0322, 0x0327, 0x0328, 0x0334,
    0x0335, 0x0336, 0x034f, 0x035c, 0x035d, 0x035e, 0x035f, 0x0360, 0x0362, 0x0338,
    0x0337, 0x0361, 0x0489
]))

MARKS_BELOW = list(map(chr, [
    0x0316, 0x0317, 0x0318, 0x0319, 0x031c, 0x031d, 0x031e, 0x031f, 0x0320, 0x0324,
    0x0325, 0x0326, 0x0329, 0x032a, 0x032b, 0x032c, 0x032d, 0x032e, 0x032f, 0x0330,
    0x0331, 0x0332, 0x0333, 0x0339, 0x033a, 0x033b, 0x033c, 0x0345, 0x0347, 0x0348,
    0x0349, 0x034d, 0x034e, 0x0353, 0x0354, 0x0355, 0x0356, 0x0359, 0x035a, 0x0323
]))

def make_zalgo_text(input_text, intensity=1.5, add_above=True, add_middle=True, add_below=True):
    """
    Transform text into zalgo text by adding combining marks
    intensity: how chaotic to make it (0 = clean, 3 = very cursed)
    """
    # Keep intensity reasonable
    if intensity < 0:
        intensity = 0
    elif intensity > 3:
        intensity = 3
    
    # Scale the number of marks based on intensity
    max_above = int(intensity * 8)
    max_middle = int(intensity * 2)  # middle marks are rarer
    max_below = int(intensity * 6)
    
    result = []
    
    for char in input_text:
        if char.isspace():
            result.append(char)
            continue
            
        zalgo_char = char
        
        if add_above and max_above > 0:
            num_marks = random.randint(0, max_above)
            for _ in range(num_marks):
                zalgo_char += random.choice(MARKS_ABOVE)
        
        if add_middle and max_middle > 0:
            num_marks = random.randint(0, max_middle)
            for _ in range(num_marks):
                zalgo_char += random.choice(MARKS_MIDDLE)
        
        if add_below and max_below > 0:
            num_marks = random.randint(0, max_below)
            for _ in range(num_marks):
                zalgo_char += random.choice(MARKS_BELOW)
        
        if len(zalgo_char) > 25:  
            zalgo_char = zalgo_char[:25]
            
        result.append(zalgo_char)
    
    return ''.join(result)

# HTML template 
HTML_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Zalgo Generator</title>
    <!-- Fun favicon using emoji -->
    <link rel="icon" type="image/svg+xml"
          href="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMjggMTI4Ij4KICA8cmVjdCB3aWR0aD0iMTI4IiBoZWlnaHQ9IjEyOCIgZmlsbD0idHJhbnNwYXJlbnQiLz4KICA8dGV4dCB4PSI1MCUiIHk9IjUwJSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZG9taW5hbnQtYmFzZWxpbmU9ImNlbnRyYWwiCiAgICAgIGZvbnQtZmFtaWx5PSJTZWdvZSBVSSBFbW9qaSBBcHBsZSBDb2xvciBFbW9qaSwgTm90byBDb2xvciBFbW9qaSIKICAgICAgZm9udC1zaXplPSI5NiI+8J+MgDwvdGV4dD4KPC9zdmc+">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        /* Dark theme because zalgo text deserves it */
        :root {
            --bg-color: #0a0b10;
            --text-color: #e8e8ff;
            --muted-color: #9aa3b2;
            --card-bg: #121420;
            --accent: #7c4dff;
            --border: #1f2433;
        }
        
        * {
            box-sizing: border-box;
        }
        
        body {
            margin: 0;
            padding: 0;
            background: var(--bg-color);
            color: var(--text-color);
            font-family: system-ui, 'Segoe UI', Roboto, Arial, sans-serif;
            font-size: 16px;
            line-height: 1.5;
        }
        
        .container {
            max-width: 900px;
            margin: 40px auto;
            padding: 20px;
        }
        
        .card {
            background: var(--card-bg);
            border: 1px solid var(--border);
            border-radius: 16px;
            padding: 20px;
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.35);
            margin-bottom: 20px;
        }
        
        h1 {
            margin: 0 0 16px 0;
            font-size: 28px;
            font-weight: 700;
        }
        
        h2 {
            margin: 0 0 8px 0;
            font-size: 20px;
        }
        
        .header-row {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 12px;
        }
        
        .main-grid {
            display: grid;
            grid-template-columns: 1fr;
            gap: 16px;
        }
        
        @media (min-width: 800px) {
            .main-grid {
                grid-template-columns: 2fr 1fr;
            }
        }
        
        label {
            display: block;
            margin: 12px 0 6px 0;
            color: var(--muted-color);
            font-weight: 500;
        }
        
        textarea, input[type="text"] {
            width: 100%;
            padding: 12px 14px;
            border-radius: 12px;
            border: 1px solid #22283a;
            background: #0e1018;
            color: var(--text-color);
            font-family: inherit;
            font-size: 14px;
        }
        
        textarea:focus, input[type="text"]:focus {
            outline: none;
            border-color: var(--accent);
        }
        
        .controls {
            display: flex;
            gap: 16px;
            align-items: center;
            flex-wrap: wrap;
            color: var(--muted-color);
            margin-top: 10px;
        }
        
        .controls label {
            margin: 0;
            display: flex;
            align-items: center;
            gap: 4px;
        }
        
        .btn {
            appearance: none;
            border: none;
            border-radius: 12px;
            background: var(--accent);
            color: white;
            padding: 12px 16px;
            font-weight: 600;
            cursor: pointer;
            font-family: inherit;
            transition: background 0.2s;
        }
        
        .btn:hover {
            background: #6c42d9;
        }
        
        .btn.secondary {
            background: #1e2233;
        }
        
        .btn.secondary:hover {
            background: #252a3f;
        }
        
        .output-box {
            background: #0e1018;
            border: 1px solid #22283a;
            border-radius: 12px;
            padding: 12px 14px;
            white-space: pre-wrap;
            word-break: break-word;
            min-height: 120px;
            font-family: monospace;
            overflow-wrap: anywhere;
        }
        
        .button-row {
            display: flex;
            gap: 8px;
            margin-top: 10px;
        }
        
        small {
            color: var(--muted-color);
        }
        
        code {
            background: #0e1018;
            padding: 2px 6px;
            border-radius: 4px;
            font-family: monospace;
        }
        
        pre {
            background: #0e1018;
            border: 1px solid #22283a;
            border-radius: 12px;
            padding: 12px;
            overflow: auto;
            margin: 12px 0;
        }
        
        .coffee-btn {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            background: #7c4dff;
            color: white;
            text-decoration: none;
            padding: 8px 12px;
            border-radius: 8px;
            font-size: 14px;
            font-weight: 500;
            transition: background 0.2s;
        }
        
        .coffee-btn:hover {
            background: #6c42d9;;
        }
        
        .coffee-icon {
            width: 16px;
            height: 16px;
            fill: currentColor;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="card">
            <div class="header-row">
                <h1>🌀 Zalgo Text Generator</h1>
            </div>
            
            <form method="post">
                <div class="main-grid">
                    <div>
                        <label for="input-text">Enter your text:</label>
                        <textarea id="input-text" name="text" rows="6" 
                                  placeholder="Type something normal here...">{{ user_text }}</textarea>
                        
                        <div class="controls">
                            <label>
                                Density: <span id="intensity-display">{{ intensity_val }}</span>
                            </label>
                            <input type="range" min="0" max="3" step="0.1" 
                                   name="density" value="{{ intensity_val }}" 
                                   oninput="document.getElementById('intensity-display').textContent=this.value">
                            
                            <label>
                                <input type="checkbox" name="up" {% if show_above %}checked{% endif %}> 
                                Above
                            </label>
                            <label>
                                <input type="checkbox" name="mid" {% if show_middle %}checked{% endif %}> 
                                Middle
                            </label>
                            <label>
                                <input type="checkbox" name="down" {% if show_below %}checked{% endif %}> 
                                Below
                            </label>
                        </div>
                    </div>
                    
                    <div>
                        <label>Cursed output:</label>
                        <div class="output-box" id="zalgo-output">{{ zalgo_result }}</div>
                        
                        <div class="button-row">
                            <button class="btn" type="submit">Summon Zalgo</button>
                            <button class="btn secondary" type="button" onclick="copyToClipboard()">Copy</button>
                        </div>
                        
                        <small>Note: Some fonts don't support all Unicode combining marks.</small>
                    </div>
                </div>
            </form>
        </div>
        
        <div class="card">
            <div class="header-row">
                <h2>API Usage</h2>
                <a href="https://www.buymeacoffee.com/blakebrandon" 
                   class="coffee-btn" target="_blank" rel="noopener">
                    <svg class="coffee-icon" viewBox="0 0 24 24">
                        <path d="M3 7h12.5a3.5 3.5 0 0 1 0 7H15.9a6.01 6.01 0 0 1-5.9 5H7a6 6 0 0 1-6-6V9a2 2 0 0 1 2-2Zm12.5 2H3v4a4 4 0 0 0 4 4h3a4 4 0 0 0 4-4h1.5a1.5 1.5 0 0 0 0-3ZM7 3.75a.75.75 0 0 1 .75-.75c.966 0 1.75.784 1.75 1.75 0 .55-.318 1.032-.66 1.45-.327.401-.59.697-.59 1.05a.75.75 0 0 1-1.5 0c0-.97.55-1.63.9-2.05.27-.33.35-.49.35-.7 0-.138-.112-.25-.25-.25A.75.75 0 0 1 7 3.75Zm3-1a.75.75 0 0 1 .75-.75c.966 0 1.75.784 1.75 1.75 0 .55-.318 1.032-.66 1.45-.327.401-.59.697-.59 1.05a.75.75 0 0 1-1.5 0c0-.97.55-1.63.9-2.05.27-.33.35-.49.35-.7 0-.138-.112-.25-.25-.25A.75.75 0 0 1 10 2.75Z"/>
                    </svg>
                    Buy me a coffee
                </a>
            </div>
            
            <p><small>Send a POST request to <code>/api/zalgo</code> with JSON data:</small></p>
            
            <pre>{
  "text": "The static is calling.",
  "density": 0.8,
  "up": true,
  "mid": true, 
  "down": true
}

Response:
{"zalgo": "T̴̲̱̭̟ͤh̜͋͠ĕ̓̀ ș̞̗͖̑́̏̋́t̙̦͛̂̋̂͐̏͘a̙̪t̢i̡̹͖̤c̀̓͛̂ͬ ĩ̂ͪͣ̓͠s̬̿̾̓ͣ͊ͪ c̸̬̣̺͒̔ȧ̬ͮͫ̌͠l̲̯ͥ͌̾ͮͦ͜ḷ͚̲̃̆̍̅͋͗i̇̋̉̃̿͏̲̹̼n̴̘̺̽͑̅̒̎̆g̣̈́ͧ͗̈͛̇͘.͉̜͕̋̽͊̅̕"}</pre>
        </div>
    </div>

    <script>
        function copyToClipboard() {
            const outputElement = document.getElementById('zalgo-output');
            const textToCopy = outputElement.textContent;
            
            navigator.clipboard.writeText(textToCopy).then(function() {
                // Show feedback
                const copyButtons = document.querySelectorAll('.btn.secondary');
                copyButtons.forEach(function(button) {
                    const originalText = button.textContent;
                    button.textContent = 'Copied!';
                    setTimeout(function() {
                        button.textContent = originalText;
                    }, 1000);
                });
            }).catch(function(err) {
                console.error('Failed to copy text: ', err);
                alert('Failed to copy text');
            });
        }
    </script>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    # Set some reasonable defaults
    user_text = ""
    intensity_val = 1.5
    show_above = True
    show_middle = True  
    show_below = True
    zalgo_result = ""

    if request.method == "POST":
        # Get form data
        user_text = request.form.get("text", "")
        
        # Parse the intensity slider
        try:
            intensity_val = float(request.form.get("density", "1.0"))
        except (ValueError, TypeError):
            intensity_val = 1.5  # fallback
            
        # Checkbox logic - they're only present if checked
        show_above = "up" in request.form
        show_middle = "mid" in request.form
        show_below = "down" in request.form
        
        # Generate the zalgo text
        if user_text.strip():  # only if there's actual text
            zalgo_result = make_zalgo_text(
                user_text, 
                intensity=intensity_val,
                add_above=show_above,
                add_middle=show_middle, 
                add_below=show_below
            )

    # Render the page with all our variables
    return render_template_string(
        HTML_PAGE,
        user_text=html.escape(user_text),
        intensity_val=intensity_val,
        show_above=show_above,
        show_middle=show_middle,
        show_below=show_below,
        zalgo_result=zalgo_result
    )

@app.route("/api/zalgo", methods=["POST"])
def zalgo_api():
    """API endpoint for generating zalgo text"""
    try:
        # Get JSON data from request
        data = request.get_json(force=True) if request.is_json else {}
        if not data:
            data = {}
            
        # Extract parameters with defaults
        text_input = data.get("text", "")
        intensity = data.get("density", 1.0)
        add_above = data.get("up", True)
        add_middle = data.get("mid", True) 
        add_below = data.get("down", True)
        
        # Convert intensity to float safely
        try:
            intensity = float(intensity)
        except (ValueError, TypeError):
            intensity = 1.5
            
        # Generate the zalgo text
        result = make_zalgo_text(
            text_input,
            intensity=intensity,
            add_above=bool(add_above),
            add_middle=bool(add_middle),
            add_below=bool(add_below)
        )
        
        return jsonify({"zalgo": result})
        
    except Exception as e:
        return jsonify({"error": "Something went wrong"}), 400

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
