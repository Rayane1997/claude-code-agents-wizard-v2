# Claude Code Agent Orchestration System v2 🚀

A simple yet powerful orchestration system for Claude Code that uses specialized agents to manage complex projects from start to finish, with mandatory human oversight, security review, and visual testing.

## 🎯 What Is This?

This is a **custom Claude Code orchestration system** that transforms how you build software projects. Claude Code itself acts as the orchestrator with its 200k context window, managing the big picture while delegating individual tasks to specialized subagents:

- **🧠 Claude (You)** - The orchestrator with 200k context managing todos and the big picture
- **✍️ Coder Subagent** - Implements one todo at a time in its own clean context
- **🔐 Cybersecurity Subagent** - Reviews implementations for OWASP risks, exposed secrets, and insecure patterns
- **👁️ Tester Subagent** - Verifies implementations using Playwright in its own context
- **🆘 Stuck Subagent** - Human escalation point when ANY problem occurs

## ⚡ Key Features

- **No Fallbacks**: When ANY agent hits a problem, you get asked - no assumptions, no workarounds
- **Security Reviews**: OWASP-focused security validation before testing begins
- **Secret Detection**: Detects exposed API keys, tokens, passwords, and unsafe configs
- **Visual Testing**: Playwright MCP integration for screenshot-based verification
- **Todo Tracking**: Always see exactly where your project stands
- **Secure Flow**: Claude creates todos → coder implements → cybersecurity reviews → tester verifies → repeat
- **Human Control**: The stuck agent ensures you're always in the loop

## 🚀 Quick Start

### Prerequisites

1. **Claude Code CLI** installed ([get it here](https://docs.claude.com/en/docs/claude-code))
2. **Node.js** (for Playwright MCP)

### Installation

```bash
# Clone this repository
git clone https://github.com/IncomeStreamSurfer/claude-code-agents-wizard-v2.git
cd claude-code-agents-wizard-v2

# Start Claude Code in this directory
claude
```

That's it! The agents are automatically loaded from the `.claude/` directory.

## 📖 How to Use

### Starting a Project

When you want to build something, just tell Claude your requirements:

```
You: "Build a todo app with React and TypeScript"
```

Claude will automatically:
1. Create a detailed todo list using TodoWrite
2. Delegate the first todo to the **coder** subagent
3. The coder implements in its own clean context window
4. Delegate security review to the **cybersecurity** subagent
5. Delegate verification to the **tester** subagent (Playwright screenshots)
6. If ANY problem occurs, the **stuck** subagent asks you what to do
7. Mark todo complete and move to the next one
8. Repeat until project complete

### The Workflow

```
USER: "Build X"
    ↓
CLAUDE: Creates detailed todos with TodoWrite
    ↓
CLAUDE: Invokes coder subagent for todo #1
    ↓
CODER (own context): Implements feature
    ↓
    ├─→ Problem? → Invokes STUCK → You decide → Continue
    ↓
CODER: Reports completion
    ↓
CLAUDE: Invokes cybersecurity subagent
    ↓
CYBERSECURITY (own context): Reviews OWASP risks, secrets, unsafe configs
    ↓
    ├─→ Security issue? → Invokes STUCK → You decide → Continue
    ↓
CYBERSECURITY: Reports success
    ↓
CLAUDE: Invokes tester subagent
    ↓
TESTER (own context): Playwright screenshots & verification
    ↓
    ├─→ Test fails? → Invokes STUCK → You decide → Continue
    ↓
TESTER: Reports success
    ↓
CLAUDE: Marks todo complete, moves to next
    ↓
Repeat until all todos done ✅
```

## 🛠️ How It Works

### Claude (The Orchestrator)
**Your 200k Context Window**

- Creates and maintains comprehensive todo lists
- Sees the complete project from A-Z
- Delegates individual todos to specialized subagents
- Tracks overall progress across all tasks
- Maintains project state and context

**How it works**: Claude IS the orchestrator - it uses its 200k context to manage everything

### Coder Subagent
**Fresh Context Per Task**

- Gets invoked with ONE specific todo item
- Works in its own clean context window
- Writes clean, functional code
- **Never uses fallbacks** - invokes stuck agent immediately
- Reports completion back to Claude

**When it's used**: Claude delegates each coding todo to this subagent

### Cybersecurity Subagent
**Fresh Context Per Security Review**

- Gets invoked after each coder completion
- Works in its own clean context window
- Reviews implementations for OWASP Top 10 vulnerabilities
- Detects exposed API keys, secrets, and tokens
- Reviews authentication, authorization, and configurations
- Blocks unsafe implementations before testing begins
- **Never approves insecure implementations**
- Reports security pass/fail back to Claude

**When it's used**: Claude delegates security review after every implementation and before testing

### Tester Subagent
**Fresh Context Per Verification**

- Gets invoked after cybersecurity approval
- Works in its own clean context window
- Uses **Playwright MCP** to see rendered output
- Takes screenshots to verify layouts
- Tests interactions (clicks, forms, navigation)
- **Never marks failing tests as passing**
- Reports pass/fail back to Claude

**When it's used**: Claude delegates testing after every approved implementation

### Stuck Subagent
**Fresh Context Per Problem**

- Gets invoked when coder, cybersecurity, or tester hits a problem
- Works in its own clean context window
- **ONLY subagent** that can ask you questions
- Presents clear options for you to choose
- Blocks progress until you respond
- Returns your decision to the calling agent
- Ensures no blind fallbacks or workarounds

**When it's used**: Whenever ANY subagent encounters ANY problem

## 🚨 The "No Fallbacks" Rule

**This is the key differentiator:**

Traditional AI: Hits error → tries workaround → might fail silently
**This system**: Hits error → asks you → you decide → proceeds correctly

Every agent is **hardwired** to invoke the stuck agent rather than use fallbacks. You stay in control.

## 💡 Example Session

```
You: "Build a landing page with a contact form"

Claude creates todos:
  [ ] Set up HTML structure
  [ ] Create hero section
  [ ] Add contact form with validation
  [ ] Style with CSS
  [ ] Test form submission

Claude invokes coder(todo #1: "Set up HTML structure")

Coder (own context): Creates index.html
Coder: Reports completion to Claude

Claude invokes cybersecurity("Review HTML structure implementation")

Cybersecurity (own context): Reviews implementation for security issues
Cybersecurity: No OWASP or secret exposure issues found
Cybersecurity: Reports success to Claude

Claude invokes tester("Verify HTML structure loads")

Tester (own context): Uses Playwright to navigate
Tester: Takes screenshot
Tester: Verifies HTML structure visible
Tester: Reports success to Claude

Claude: Marks todo #1 complete ✓

Claude invokes coder(todo #2: "Create hero section")

Coder (own context): Implements hero section
Coder: ERROR - image file not found
Coder: Invokes stuck subagent

Stuck (own context): Asks YOU:
  "Hero image 'hero.jpg' not found. How to proceed?"
  Options:
  - Use placeholder image
  - Download from Unsplash
  - Skip image for now

You choose: "Download from Unsplash"

Stuck: Returns your decision to coder
Coder: Proceeds with Unsplash download
Coder: Reports completion to Claude

... and so on until all todos done
```

## 📁 Repository Structure

```
.
├── .claude/
│   ├── CLAUDE.md                  # Orchestration instructions for main Claude
│   └── agents/
│       ├── coder.md              # Coder subagent definition
│       ├── cybersecurity.md      # Cybersecurity review agent definition
│       ├── tester.md             # Tester subagent definition
│       └── stuck.md              # Stuck subagent definition
├── .mcp.json                      # Playwright MCP configuration
├── .gitignore
└── README.md
```

## 🎓 Learn More

### Resources

- **[SEO Grove](https://seogrove.ai)** - AI-powered SEO automation platform
- **[ISS AI Automation School](https://www.skool.com/iss-ai-automation-school-6342/about)** - Join our community to learn AI automation
- **[Income Stream Surfers YouTube](https://www.youtube.com/incomestreamsurfers)** - Tutorials, breakdowns, and AI automation content

### Support

Have questions or want to share what you built?
- Join the [ISS AI Automation School community](https://www.skool.com/iss-ai-automation-school-6342/about)
- Subscribe to [Income Stream Surfers on YouTube](https://www.youtube.com/incomestreamsurfers)
- Check out [SEO Grove](https://seogrove.ai) for automated SEO solutions

## 🤝 Contributing

This is an open system! Feel free to:
- Add new specialized agents
- Improve existing agent prompts
- Share your agent configurations
- Submit PRs with enhancements

## 📝 How It Works Under the Hood

This system leverages Claude Code's [subagent system](https://docs.claude.com/en/docs/claude-code/sub-agents):

1. **CLAUDE.md** instructs main Claude to be the orchestrator
2. **Subagents** are defined in `.claude/agents/*.md` files
3. **Each subagent** gets its own fresh context window
4. **Main Claude** maintains the 200k context with todos and project state
5. **Playwright MCP** is configured in `.mcp.json` for visual testing

The magic happens because:
- **Claude (200k context)** = Maintains big picture, manages todos
- **Coder (fresh context)** = Implements one task at a time
- **Cybersecurity (fresh context)** = Reviews OWASP risks and secret exposure
- **Tester (fresh context)** = Verifies one implementation at a time
- **Stuck (fresh context)** = Handles one problem at a time with human input
- **Each subagent** has specific tools and hardwired escalation rules

## 🎯 Best Practices

1. **Trust Claude** - Let it create and manage the todo list
2. **Review security findings** - The cybersecurity agent validates implementation safety
3. **Review screenshots** - The tester provides visual proof of every implementation
4. **Make decisions when asked** - The stuck agent needs your guidance
5. **Don't interrupt the flow** - Let subagents complete their work
6. **Check the todo list** - Always visible, tracks real progress

## 🔥 Pro Tips

- Use `/agents` command to see all available subagents
- Claude maintains the todo list in its 200k context - check anytime
- Security reviews happen before testing begins
- Screenshots from tester are saved and can be reviewed
- Each subagent has specific tools - check their `.md` files
- Subagents get fresh contexts - no context pollution!

## 📜 License

MIT - Use it, modify it, share it!

## 🙏 Credits

Built by [Income Stream Surfer](https://www.youtube.com/incomestreamsurfers)

Powered by Claude Code's agent system and Playwright MCP.

---

**Ready to build something amazing securely?** Just run `claude` in this directory and tell it what you want to create! 🚀
