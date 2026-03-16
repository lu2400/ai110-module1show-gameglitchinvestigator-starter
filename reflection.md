# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

1. the hints would give the wrong hint (saying to go low when the number was higher)
the hints should accurately tell the user if to go higher or lower
2. the attempts number not updating accurately (it wasn't counting for some of my attempts)
number should accurately let the user know how many attempts they have left
3. starting a new game doesnt reset or clear history
starting a new game should clear the previous game's history

i described the backwards hint bug 
AI let me know that the outcome labels were correct but the hint message was backwards for a higher or lower guess relative to the actual number

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

I used Claude. When prompted with the bugs I had found myself, it pointed me to the specifics of why each bug didn't work. For example, i thought the attempts bug was just not counting down but it let me know it was buggy on even numbers.
After verifying what it changed VERY carefully, it actually didn't do anything wrong or misleading. Granted, I had to check through everything it changed line by line. 
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?
i used the tests file to make sure the bugs i fixed worked as intended. i manually went to check the region of the error and used a pen and paper to map out the logic to make sure it was fixed successfully. I also checked the edits Clause made line by line to verify.
---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
