# Technical Case Study: Solving Agentic Hallucinations in Portfolio UI

## Problem Space

While building this engineering portfolio using autonomous coding agents, we encountered "agentic hallucinations" where the AI would aggressively overwrite image paths with external placeholder URLs or stretch images to `100% width`, completely breaking the visual grid layout. Furthermore, the agent often suggested uploading images to Imgur or other external hosting rather than utilizing a clean, local file structure.

## The Solution: Contract-Based Design Systems and Local Skills

To establish a strict boundary and prevent these hallucinations, we integrated **Awesome Design MD** and **Firecrawl CLI** as local "skills" within the agent's workspace.

### Key Actions Taken

1. **Local Skill Integration**: Added local clones of essential agentic skills into the `/tools` directory, creating a offline knowledge base the agent could read from without external web-searching errors.
2. **Implementing a `DESIGN.md` Contract**: We adopted the `Awesome Design MD` paradigm by writing a deterministic `DESIGN.md` file in our root directory. This acts as a source-of-truth style guide.
3. **Strict Constraints**: 
   - Forced local paths originating from `/images`.
   - Enforced hard constraints on image dimensions (`width: 600px`, `object-fit: cover`) to avoid layout blowouts.
   - Strictly prohibited the use of Imgur or external asset CDNs to preserve privacy and asset locality.

## Results

By establishing a clear, document-based contract (`DESIGN.md`), the AI agent was forced to conform to deterministic layout limits and local file references. This stabilized the UI development process, improved image consistency, and demonstrated an advanced methodology for managing and directing non-deterministic LLMs in front-end development workflows.
