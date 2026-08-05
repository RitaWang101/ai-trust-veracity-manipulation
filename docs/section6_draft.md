# Section 6 Representative Module Drafts

## Veracity

The Veracity module operationalizes epistemic correctness through 14 single-turn probes spanning factual accuracy, hallucination detection, appropriate uncertainty, misleading-premise detection, and context verification. The current prompt set is derived from the Lab's validated Veracity artifact and is evaluated using a hybrid score that combines deterministic checks (50%) with an LLM-as-judge assessment (50%). Deterministic checks identify expected factual anchors, explicit correction of false premises, uncertainty language, and requests for missing temporal or entity context. The judge evaluates whether the response is factually correct, avoids unsupported details, identifies all material errors in a misleading premise, and calibrates certainty to the information available. Raw failure indicators are converted to a trust-oriented score and normalized to the framework's 0–100 module scale. Prompt review indicates that the baseline is suitable for pilot testing, subject to rubric clarification for fictional-entity probes, live-information questions, compounded-error prompts, and context-dependent queries. Verified cross-model findings are not yet available in the reviewed artifacts; the final paper should report per-aspect performance and at least one representative comparison after the validated set is executed through the current evaluation runner.

## Manipulation

The Manipulation module evaluates preservation of user autonomy under influence pressure. The current 11-prompt baseline combines single-turn probes, mirrored political framings, and multi-turn escalation, with a hybrid score weighted 25% deterministic heuristic and 75% LLM-as-judge. Review of the baseline shows that most prompts currently test User-to-Model pressure resistance, including demands for certainty, unsafe advice, factual capitulation, and emotional dependency. To align the module with its stated objective of protecting users from manipulative AI behavior, the methodology should use two complementary layers: User-to-Model resistance and Model-to-User non-manipulation. The second layer should test whether a model avoids coercive or autonomy-reducing tactics such as guilt, fear, false urgency, false promises, stigmatization, social proof, induced self-doubt, and induced doubt about the environment. Deterministic checks identify high-risk markers, while the judge evaluates coercion, transparency of intent, preservation of choice, proportionality, and safe redirection. Several baseline items require revision because they overlap with Candor or lack a manipulation mechanism. Accordingly, the present text documents a validated redesign specification rather than claiming completed experimental results. Final Section 6 results should be added only after both layers are implemented, peer-reviewed, and run on at least two models.

## Result table placeholder

`Model | Module | Aspect/Layer | N Prompts | Heuristic Score | Judge Score | Normalized Score | Key Failure Pattern`

Do not report a Trust Index until every included module score has been verified and the aggregation weights are stated.

