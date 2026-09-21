# Lab 1 — Zulpaidar Aiganym

## 1. Part 1 Prediction and Part 2 Reference Result

Before Part 2, I used UTF-8 bytes for my prediction. Russian had 576 bytes and English had 300 bytes. Kazakh had 640 bytes.

| Ratio | My prediction | Reference result |
|---|---:|---:|
| RU / EN | 1.92x | 1.46x |
| KK / EN | 2.13x | 2.15x |

**Note:** I did not have the classroom API key. So I used the teacher's reference file, `measurements.example.json`, for Part 2.

The Russian miss is the real lesson. Russian and Kazakh use almost the same bytes per letter (1.83 and 1.86), but their token ratios are very different (1.46x and 2.15x). So a tokenizer does not follow bytes. It follows its own table of common text pieces (the merge table), and Russian pieces are more common in that table than Kazakh ones. My Kazakh prediction was close mostly by chance.

## 2. Annual Cost

I use 5,000 support requests per day (1,825,000 per year). My assumption: a Kazakh bank with 1.5 million active customers, where 10% contact support once a month, gets 150,000 requests per month, which is about 5,000 per day.

| Model | English | Russian | Kazakh |
|---|---:|---:|---:|
| Haiku 4.5 | $8,979 | $11,569 | $12,779 |
| Sonnet 5 | $17,958 | $23,137 | $25,557 |
| Opus 5 | $44,895 | $57,843 | $63,893 |
| Fable 5.1 | $89,790 | $115,687 | $127,786 |

**Important:** Kazakh input is 2.19x English in tokens, but the Kazakh total bill is only 1.42x English, on every model. Output tokens are about 95% of the bill, and the answers grow less than the questions. The table uses answer lengths measured on Opus 5 in the reference run.

## 3. Model for a Kazakh Support Queue

Cost does not decide this choice; quality does. For Kazakh at my volume, Opus 5 costs about $51,000 per year more than Haiku 4.5. That number is the most that quality can cost me. The risk is on the other side: the complaint says a contract is attached, but nothing is attached, so a good answer must say it cannot explain the rate change. A model that invents a reason breaks the system prompt, and in a bank that means wrong information to a customer.

My choice: I start with Opus 5 as the safe default. Then I test Haiku 4.5, Sonnet 5 and Opus 5 on Kazakh answers with a checklist I fix before I see any answer (taken from README Task 7):  
1. does not invent the reason for the rate change;  
2. invents no numbers;  
3. answers only in Kazakh;  
4. gives a clear next step.

I move to the cheapest model that passes all four checks on every test answer.

**Note:** the Haiku and Sonnet costs in my table assume the same answer length as Opus 5. This is not measured.

## 4. One Cost-Reduction Lever

Capping the answer length (for example, adding “Answer in at most two sentences” to the system prompt) would cut output tokens, which cost 5x more than input on every model and are about 95% of the Kazakh bill.

## GitHub

https://github.com/aiganymzulpaidar-svg/lab-01-AI-course

---

# AI-USE DECLARATION

I used ChatGPT to help me understand the lab instructions.

My Part 1 prediction was written before Part 2. I did not have the classroom API key, so I used the teacher's reference file for the Part 2 numbers. I did not present these numbers as my own API measurement.

I used Claude to review my draft. It re-ran `part1_offline.py` and `part3_cost.py` to check my numbers and suggested changes to sections 1–4. I checked all numbers against the course files myself.
