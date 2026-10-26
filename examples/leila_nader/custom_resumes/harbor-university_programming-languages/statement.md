# Leila Nader
Programming languages
Harbor City | leila.nader@example.com

I want to study how a compiler can explain a type error so that a student can repair it. My master's thesis built a teaching language whose stepper shows each type-checking rule as it fires. Dr. Jonah Hale supervised that work at Harbor University. The workshop paper we wrote describes the stepper. What the thesis did not do is measure whether seeing the rule helps a student choose a fix. That measurement is the doctoral project.

The language is small on purpose. A program is a handful of definitions, and the type checker walks a short list of rules. When a rule fails, the stepper stops and prints the rule, the subterm, and the environment. I implemented that walk in OCaml. I sat with students who were meeting type inference for the first time and watched where they got stuck. They could repeat the rule. They often could not say which expression to change. The tool showed the failure and stopped there.

I chose this problem because the courses I had taken treated a type checker as a finished artifact. The interesting part, once the checker exists, is the explanation it owes the person who wrote the program. Building the stepper taught me to keep the rules and the implementation in correspondence. It also showed me the limit of a tool that only prints a rule name. A doctoral project can add the missing piece: a suggestion for the edit, tested with students, without claiming that the current stepper already teaches better than an ordinary error.

Harbor is where I want to do that work. The programming-languages group builds languages and the tools around them, and my preparation matches that work: the thesis, the OCaml implementation, and the paper with Dr. Hale. I am not asking to join a particular lab as if a supervisor had already agreed. I am asking to be trained to turn this stepper into a study of explanations.

The GPA on my master's transcript is 3.7/4.0, and the bachelor's GPA is 3.4/4.0. Those numbers are the record. The preparation I want considered is the thesis and the paper. I can send the workshop paper and the stepper to anyone on the committee who wants to read the rules.
