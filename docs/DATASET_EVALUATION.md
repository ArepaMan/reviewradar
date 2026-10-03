# Phase 1: dataset evaluation (work in progress)

The owner is evaluating four candidates one at a time, then decides. Record the final choice in `docs/DECISIONS.md`. Evidence below comes from the owner's screenshots and notes, not from verified downloads. Claude could not open dataset pages from the cloud session (network blocked), so anything marked "unverified" must be checked by the owner.

## Criteria (agreed in chat)
1. **Label meaning:** does the label correspond to a real triage or routing decision?
2. **Text realism:** real, messy text versus templated or synthetic text (synthetic text can make baselines look unrealistically good).
3. **Difficulty and balance:** hard enough to show a transformer beating TF-IDF, but not mostly noise; class balance.
4. **Size and cost:** fits a laptop and free GPUs; works with Postgres in Phase 1.
5. **License:** safe for a public portfolio repo.
6. **Fit with later phases:** SQL practice (Phase 1), RAG over documents (Phase 4), drift over time (Phase 6).

## Candidates and status
| Dataset | Status | Link |
|---|---|---|
| Amazon Reviews 2023 | Evidence collected (below) | https://huggingface.co/datasets/McAuley-Lab/Amazon-Reviews-2023 and https://amazon-reviews-2023.github.io/ |
| Bitext customer support | Partial evidence (below); still missing sample rows as text | https://huggingface.co/datasets/bitext/Bitext-customer-support-llm-chatbot-training-dataset |
| Banking77 | Evidence collected (below); sample rows still missing | https://huggingface.co/datasets/PolyAI/banking77 |
| CFPB Consumer Complaint Database | Waiting | https://www.consumerfinance.gov/data-research/consumer-complaints/ |

What to collect for each remaining candidate: license text, row count, column names, the label list or label count, and 15-20 sample rows pasted as text. For CFPB also: which column is the label (Product or Issue) and how many narratives exist. Do not commit data files (`data/*/*` is ignored).

## Amazon Reviews 2023: evidence so far
- Fields (reviews): `rating` (1.0-5.0), `title`, `text`, `images`, `asin`, `parent_asin`, `user_id`, `timestamp` (unix), `verified_purchase`, `helpful_vote`.
- Fields (item metadata): `main_category`, `title`, `average_rating`, `rating_number`, `features`, `description`, `price`, `images`, `videos`, `store`, `categories` (hierarchical), `details`, `parent_asin`, `bought_together`. Reviews join to products on `parent_asin`.
- Size: split by category. Small ones: Subscription_Boxes about 16K ratings, Magazine_Subscriptions about 71K, Digital_Music about 130K, Gift_Cards about 152K. Huge ones: Clothing_Shoes_and_Jewelry about 66M, Books about 29.5M. Any category used needs a sample.
- Average review length (tokens / ratings from the dataset card table): Video_Games about 76, Grocery_and_Gourmet_Food about 41, Toys_and_Games about 43. Averages hide the long tail: compute median and p90/p99 in EDA before choosing a model max length (128 vs 256 vs 512).
- License: the owner found no explicit license (described as for academic or educational use; unverified). Safe practice: never redistribute the data, cite the paper, tell readers to download it themselves.
- Citation: Hou, Yupeng; Li, Jiacheng; He, Zhankui; Yan, An; Chen, Xiusi; McAuley, Julian. "Bridging Language and Items for Retrieval and Recommendation". arXiv:2403.03952, 2024.
- Owner's tentative category if Amazon wins: Toys_and_Games (variety of product types). Caveat: 16.3M ratings, must sample (about 100K-200K).

Scorecard (Claude's view so far):
| Criterion | Amazon |
|---|---|
| Label meaning | Weak: rating is sentiment, not triage; the task would have to be defined (for example flag 1-2 star reviews, or predict subcategory from `categories`) |
| Text realism | Strong |
| Difficulty and balance | Moderate: ratings are noisy, 5 stars dominate (imbalanced) |
| Size and cost | OK only with one category and a sample |
| Phase 1 fit (SQL, Postgres) | Very strong: real relational structure, joins on `parent_asin` |
| Later phases | Strong: product descriptions for RAG, timestamps (1996-2023) for drift |
| License | Unclear |

## Bitext customer support: evidence so far
- Fields: `flags` (language-generation tags), `instruction` (the customer's request, the text to classify), `category` (11 high-level), `intent` (the fine label), `response` (an example assistant reply).
- Specs from the card: use case intent detection, vertical customer service, 27 intents in 11 categories (confirmed on the dataset viewer: `intent` 27 values, `category` 11 values; `flags` 394 values), 26,872 question/answer pairs (about 1,000 per intent), 30 entity/slot types, 12 language-generation tags.
- Categories in my cropped screenshot (10 of 11): ACCOUNT, CANCELLATION_FEE, DELIVERY, FEEDBACK, INVOICE, NEWSLETTER, ORDER, PAYMENT, REFUND, SHIPPING_ADDRESS.
- Intents shown in the screenshot: 20 (create_account, delete_account, edit_account, switch_account, check_cancellation_fee, delivery_options, complaint, review, check_invoice, get_invoice, newsletter_subscription, cancel_order, change_order, place_order, check_payment_methods, payment_issue, check_refund_policy, track_refund, change_shipping_address, set_up_shipping_address). The viewer shows 27 intent values, so the screenshot was cropped. Resolved.
- License: cdla-sharing-1.0 (Community Data License Agreement, sharing). Permissive enough for use and for sharing derived work under the same terms; owner should read it once and note the attribution/sharing conditions.
- Owner's sample (all `cancel_order`): short texts (6-92 characters), template slots like `{{Order Number}}` left in the text, injected typos (`oorder`, `puchase`), synonym swaps (`purchase` for `order`). Conclusion: synthetic, generator-made, and train and test come from the same generator, so TF-IDF should score very high (owner guessed 85%, Claude guessed high 90s; test it in the baseline). Still needed (optional): rows from other intents, and whether the data is synthetic (the card says it is generated; confirm the wording).

Scorecard (Claude's view so far, Bitext):
| Criterion | Bitext |
|---|---|
| Label meaning | Strong: intent and category are routing decisions (which team or flow handles this) |
| Text realism | Probably weak: generated from templates, likely clean and repetitive (confirm with samples) |
| Difficulty and balance | Probably too easy: about 1,000 per intent, so balanced, but a TF-IDF model may score near the ceiling and leave no room to show a transformer |
| Size and cost | Excellent: 26,872 rows, trivial for a laptop |
| Phase 1 fit (SQL, Postgres) | Weak: one flat table, nothing to join |
| Later phases | Medium: `response` could seed RAG answers, but there are no timestamps, so drift would have to be simulated |
| License | Good: cdla-sharing-1.0 |

## Banking77: evidence so far
- Source: PolyAI; Casanueva et al. 2020, "Efficient Intent Detection with Dual Sentence Encoders", arXiv:2003.04807 (ACL 2020 NLP for ConvAI workshop). Data also at https://github.com/PolyAI-LDN/task-specific-datasets.
- Fields: `text` (string) and `label` (integer 0-76, so 77 intents). Example: label 11 = `card_arrival`, text "I am still waiting on my card?".
- Size: train 10,003, test 3,080 (the card table). Average length 59.5 characters (train), 54.2 (test). One domain (banking). English.
- License: CC BY 4.0 (attribution required; fine for a public repo with citation).
- Labels seen: activate_my_card, age_limit, apple_pay_or_google_pay, atm_support, automatic_top_up, balance_not_updated_after_bank_transfer, card_arrival, card_not_working, card_swallowed, cash_withdrawal_charge, change_pin and more (only the first 22 were screenshotted). Many intents are close neighbours (several about card payments, several about balances and top-ups).
- Still needed: 15-20 rows from different labels; whether the texts are real customer queries (the paper says crowd-sourced, unverified).

Scorecard (Claude's view so far, Banking77):
| Criterion | Banking77 |
|---|---|
| Label meaning | Strong: intent is what the customer wants (a routing or answer decision), though 77 fine labels is more granular than a real triage queue; could be grouped |
| Text realism | Medium-good: short single-sentence queries written by people, so varied wording (unverified, check the rows) |
| Difficulty and balance | Good: 77 close classes, known to be hard enough for a transformer to clearly beat TF-IDF on rare phrasing; train is imbalanced (some intents have far fewer examples; owner to confirm in EDA) |
| Size and cost | Excellent: about 13K rows, laptop-sized, fast to fine-tune |
| Phase 1 fit (SQL, Postgres) | Weak: one flat table of text and label, nothing to join |
| Later phases | Medium: no timestamps, so drift must be simulated; no document corpus for RAG (would need to write or source help articles) |
| License | Good: CC BY 4.0 |

## Next
Owner sends CFPB evidence next (Bitext and Banking77 collected; sample rows from several labels still optional). Claude compares all four on the same criteria; the owner decides and writes a one-paragraph justification; then the decision goes into `DECISIONS.md`.
