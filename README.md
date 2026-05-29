Business Context
It’s a typical Monday morning inside a large consumer electronics support operations center (Samsung-like ecosystem).

Over the weekend, thousands of customer queries have accumulated:

A Galaxy device overheating after a recent update

A customer confused between two newly launched smartphone models

A support agent searching for a troubleshooting step buried inside lengthy product manuals

Inside the support system:

Information is scattered across PDFs, FAQs, and internal knowledge bases

Agents switch between multiple tools to find answers

Similar queries are handled repeatedly

Response times are increasing

As the product ecosystem expands, support operations become more complex. Customers now expect instant, accurate, and context-aware assistance.

The Turning Point
The CTO states:

“We don’t need more data. We need a system that can intelligently use it.”

Objective
Design and build a Smart Support Copilot using Generative AI that:

Understands user queries

Retrieves relevant knowledge using RAG

Maintains conversational context

Dynamically adapts its response based on query type

Produces structured, actionable outputs

Problem Statement
Existing systems struggle because they:

Cannot differentiate between types of queries

Treat all questions the same way

Fail to provide structured, actionable responses

Do not maintain context across interactions

Core Challenge
How can we build an intelligent system that not only answers queries but alsodecides how to answer them based on user intent?

Expectations (What You Need to Build)
1. Conversational Interface (Baseline)
Streamlit-based chat UI

Maintain chat history

Support follow-up queries

2. Retrieval-Augmented Generation (RAG)
Upload PDFs (manuals, FAQs)

Chunk + embed documents

Retrieve relevant context (FAISS)

Generate grounded responses

3. Query Classification Layer 
Your system must classify the query before answering.

Required Query Types:
Troubleshooting

Product Comparison

General Knowledge

Implementation Options:
Rule-based (keywords)

Prompt-based classification (LLM)

4. Dynamic Response Routing 
Based on query type, your system must:

Change response structure

Use different prompts

Example:
Query Type	Behavior
Troubleshooting	Step-by-step resolution
Comparison	Table / structured comparison
General	Direct explanation

5. Structured Response Generation 

Responses must follow strict formats.

Troubleshooting Format:
Possible Causes

Step-by-Step Solution

When to Escalate

Comparison Format:
Feature Comparison Table

Key Differences

Recommendation

General Query:
Direct Answer

Explanation

Additional Notes

6. Context Awareness

Use chat history

Handle follow-up queries

Avoid repetition

Example:

User:

“What about battery issue?”

System should:
Understand previous context (phone discussion)

7. Confidence / Source Awareness 
Your response should include:

Source reference (from retrieved docs)
OR

Confidence hint (e.g., “Based on available documents…”)

Expected Output

A working system that:

Handles multiple query types intelligently

Uses RAG for grounded answers

Dynamically adapts responses

Produces structured outputs

Maintains conversational context

Sample Queries
“Why is my Galaxy phone overheating?”

“Compare Galaxy S23 vs S24”

“How to reset Samsung Smart TV?”

“What if this keeps happening?”(follow-up)