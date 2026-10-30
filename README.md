Unlike machine learning models that you train from scratch, this application uses API-driven cloud intelligence through Prompt Engineering. The data follows a direct processing pipeline:

The Input (Data): Raw human-written text provided by the user via the frontend workspace.

The Context (System Prompt): Explicit boundaries injected into the application script that dictate how the AI should behave (acting as a strict linguistic classifier).

The Inference (Cloud Computation): The pre-trained large language model processes the combined context over an API connection.

The Output (Web UI): Streamlit intercepts the raw generation string and structures it cleanly using Markdown layouts and matching emojis.
