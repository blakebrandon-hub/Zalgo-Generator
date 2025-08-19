# Zalgo Text Generator 🌀

A Flask web app that transforms normal text into cursed zalgo text using Unicode combining marks. Perfect for when you need to s̸u̷m̶m̴o̸n̵ ̷t̶h̸e̴ ̵v̷o̶i̸d̴ or just mess with your friends.

## What is Zalgo Text?

Zalgo text (also known as "cursed text" or "glitch text") uses Unicode combining characters to create text that appears corrupted or glitched. It's named after the creepypasta character Zalgo and has become popular in memes and social media.

## Features

- **Web Interface**: Clean, dark-themed UI for generating zalgo text
- **Customizable Chaos**: Adjust intensity from barely noticeable to completely unreadable  
- **Direction Control**: Toggle marks above, middle, or below characters independently
- **REST API**: Programmatic access via JSON endpoints
- **Copy to Clipboard**: One-click copying of generated text
- **Mobile Friendly**: Responsive design that works on phones and tablets

## Usage

### Web Interface

1. Type your text in the input box
2. Adjust the "Chaos level" slider (0 = clean, 3 = maximum cursedness)
3. Choose which directions to add marks (above/middle/below)
4. Click "Generate Zalgo" 
5. Copy the result and unleash chaos upon the world

### API Usage

Send a POST request to `/api/zalgo` with JSON data:

```bash
curl -X POST http://localhost:5000/api/zalgo \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Hello world",
    "density": 1.5,
    "up": true,
    "mid": true,
    "down": true
  }'
```

Response:
```json
{
  "zalgo": "Ḧ̴̰e̷̲͝l̶̰̔l̴̰̈ȯ̶̰ ̴̰̈w̷̲͝ő̶̰r̴̰̈l̶̰̔d̷̲͝"
}
```

#### API Parameters

- `text` (string): The text to transform
- `density` (float, 0-3): How chaotic to make it. Default: 1.5
- `up` (boolean): Add marks above characters. Default: true  
- `mid` (boolean): Add marks through the middle. Default: true
- `down` (boolean): Add marks below characters. Default: true

## Examples

**Light zalgo** (density: 0.5):
```
H̃ello w̃orld
```

**Medium zalgo** (density: 1.5):
```
Ḧ̴̰e̷̲͝l̶̰̔l̴̰̈ȯ̶̰ ̴̰̈w̷̲͝ő̶̰r̴̰̈l̶̰̔d̷̲͝
```

**Maximum chaos** (density: 3.0):
```
Ḧ̷̢̧̡̛̖̰̮̘̪̫̳̗̰̼̯̭̺̟̤̜̱̠̩́̓̽̏͂̈́̈́̉̆̎̎̈́̽̊̏̊̅̍̅̌͌̑̎̂̂̃̈́̎̏̍̓̇̇̈́̈́̍̃̂̋͋͋̊̌̃͑̏̚̚͘͜ë̴́l̴l̴o̴ ̴w̴ő̴r̴l̴d̴
```

## How It Works

The app uses Unicode combining marks (diacritical marks) that are designed to modify other characters. By adding multiple combining marks to each character, we create the "corrupted" zalgo effect.

There are three types of marks:
- **Above**: Marks that appear above the base character (accents, tildes, etc.)
- **Middle**: Marks that go through the character (strikethrough-like effects)  
- **Below**: Marks that appear below the base character (cedillas, underlines, etc.)

The algorithm randomly selects marks from each category based on the specified intensity level.

## Technical Details

- **Backend**: Flask (Python)
- **Frontend**: Vanilla HTML/CSS/JavaScript
- **Unicode Ranges**: Uses combining marks from various Unicode blocks
- **Safety Limits**: Prevents extremely long strings that could break browsers
- **Error Handling**: Graceful fallbacks for invalid input

## Font Compatibility

Not all fonts support every Unicode combining mark. For best results, use fonts with good Unicode support like:
- System fonts (they usually work well)
- Google Fonts with extensive character sets
- Noto fonts (designed for comprehensive Unicode coverage)

## License

This project is open source. Do whatever you want with it, just don't blame me if you accidentally summon an eldritch horror.

## Warning ⚠️

Use responsibly! Zalgo text can:
- Be difficult to read for people with dyslexia or visual impairments
- Break some older systems or applications  
- Get your messages flagged as spam on some platforms
- Cause existential dread in typography enthusiasts

---

*"He comes"* - Zalgo
