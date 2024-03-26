import json
import random

from openai import OpenAI
from openai.types.chat.chat_completion import ChatCompletion
from ._config import ValidatorSettings


def get_themes():

    themes = [
        "artificial intelligence",
        "machine learning",
        "deep learning",
        "natural language processing",
        "computer vision",
        "robotics",
        "neural networks",
        "data science",
        "big data",
        "data mining",
        "data analytics",
        "cloud computing",
        "edge computing",
        "quantum computing",
        "distributed systems",
        "parallel computing",
        "high-performance computing",
        "supercomputers",
        "computer architecture",
        "microprocessors",
        "semiconductors",
        "integrated circuits",
        "Moore's Law",
        "embedded systems",
        "IoT (Internet of Things)",
        "wireless sensor networks",
        "5G networks",
        "software engineering",
        "agile development",
        "DevOps",
        "version control systems",
        "programming languages",
        "object-oriented programming",
        "functional programming",
        "scripting languages",
        "web development",
        "front-end development",
        "back-end development",
        "full-stack development",
        "mobile app development",
        "cross-platform development",
        "game development",
        "virtual reality",
        "augmented reality",
        "computer graphics",
        "3D modeling",
        "animation",
        "rendering",
        "database management systems",
        "SQL databases",
        "NoSQL databases",
        "data warehousing",
        "data lakes",
        "data pipelines",
        "ETL (Extract, Transform, Load)",
        "data visualization",
        "business intelligence",
        "machine learning ops (MLOps)",
        "DevSecOps",
        "cybersecurity",
        "network security",
        "cryptography",
        "blockchain",
        "smart contracts",
        "decentralized applications (dApps)",
        "operating systems",
        "Linux",
        "Unix",
        "Windows",
        "macOS",
        "virtualization",
        "containerization",
        "Docker",
        "Kubernetes",
        "serverless computing",
        "microservices architecture",
        "API development",
        "RESTful APIs",
        "GraphQL",
        "web servers",
        "load balancing",
        "caching",
        "content delivery networks (CDN)",
        "computer networks",
        "network protocols",
        "TCP/IP",
        "HTTP",
        "HTTPS",
        "FTP",
        "DNS",
        "DHCP",
        "VPN",
        "software testing",
        "unit testing",
        "integration testing",
        "system testing",
        "performance testing",
        "usability testing",
        "test automation",
        "continuous integration",
        "continuous delivery",
        "software maintenance",
        "legacy systems",
        "software migration",
        "software modernization",
        "IT infrastructure",
        "data centers",
        "server hardware",
        "storage systems",
        "backup and recovery",
        "disaster recovery",
        "high availability",
        "fault tolerance",
        "scalability",
        "performance optimization",
        "computer history",
        "mainframes",
        "minicomputers",
        "personal computers",
        "mobile computing",
        "internet history",
        "World Wide Web",
        "e-commerce",
        "social media",
        "digital transformation",
        "industry 4.0",
        "smart factories",
        "predictive maintenance",
        "computer ethics",
        "AI ethics",
        "data privacy",
        "GDPR",
        "accessibility",
        "digital divide",
        "tech for good",
        "green computing",
        "e-waste",
        "sustainable technology",
        "human-computer interaction",
        "user experience (UX)",
        "user interface (UI) design",
        "information retrieval",
        "search engines",
        "recommender systems",
        "chatbots",
        "conversational AI",
        "sentiment analysis",
        "text mining",
        "image processing",
        "pattern recognition",
        "speech recognition",
        "biometrics",
        "lambda calculus",
        "combinatory logic",
        "type theory",
        "category theory",
        "homotopy type theory",
        "proof assistants",
        "Coq theorem prover",
        "Agda programming language",
        "Idris programming language",
        "dependent types",
        "linear types",
        "session types",
        "substructural type systems",
        "graph rewriting",
        "term rewriting",
        "abstract rewriting systems",
        "compiler design",
        "lexical analysis",
        "parsing",
        "abstract syntax trees",
        "intermediate representations",
        "code generation",
        "static analysis",
        "data-flow analysis",
        "control-flow analysis",
        "type inference",
        "abstract interpretation",
        "program optimization",
        "loop optimizations",
        "instruction scheduling",
        "register allocation",
        "garbage collection",
        "memory management",
        "virtual machines",
        "just-in-time compilation",
        "ahead-of-time compilation",
        "partial evaluation",
        "program synthesis",
        "inductive programming",
        "probabilistic programming",
        "constraint programming",
        "logic programming",
        "answer set programming",
        "Prolog",
        "Datalog",
        "Curry–Howard correspondence",
        "intuitionistic logic",
        "constructive mathematics",
        "formal verification",
        "model checking",
        "temporal logic",
        "linear temporal logic",
        "computation tree logic",
        "process calculi",
        "π-calculus",
        "actor model",
        "communicating sequential processes",
        "petri nets",
        "colored petri nets",
        "workflow nets",
        "process mining",
        "business process management",
        "BPMN (Business Process Model and Notation)",
        "YAWL (Yet Another Workflow Language)",
        "process-aware information systems",
        "transactional memory",
        "software transactional memory",
        "hardware transactional memory",
        "concurrent data structures",
        "lock-free data structures",
        "wait-free data structures",
        "consensus algorithms",
        "Paxos algorithm",
        "Raft algorithm",
        "Byzantine fault tolerance",
        "distributed consensus",
        "gossip protocols",
        "epidemic protocols",
        "distributed hash tables",
        "peer-to-peer networks",
        "content-addressable networks",
        "distributed file systems",
        "MapReduce",
        "Hadoop",
        "Apache Spark",
        "stream processing",
        "complex event processing",
        "reactive programming",
        "functional reactive programming",
        "event-driven architectures",
        "message-oriented middleware",
        "enterprise service bus",
        "service-oriented architecture",
        "business rules engines",
        "expert systems",
        "knowledge representation",
        "description logics",
        "ontologies",
        "semantic web",
        "linked data",
        "RDF (Resource Description Framework)",
        "SPARQL",
        "OWL (Web Ontology Language)",
        "rule-based systems",
        "forward chaining",
        "backward chaining",
        "Rete algorithm",
        "fuzzy logic",
        "rough sets",
        "evolutionary algorithms",
        "genetic algorithms",
        "genetic programming",
        "swarm intelligence",
        "ant colony optimization",
        "particle swarm optimization",
        "simulated annealing",
        "tabu search",
        "combinatorial optimization",
        "constraint satisfaction",
        "SAT solvers",
        "SMT solvers",
        "automated reasoning",
        "automated theorem proving",
        "computer algebra systems",
        "symbolic computation",
        "numerical analysis",
        "finite element analysis",
        "computational fluid dynamics",
        "molecular dynamics",
        "Monte Carlo methods",
        "stochastic simulation",
        "agent-based modeling",
        "cellular automata",
        "complex networks",
        "graph theory",
        "network science",
        "small-world networks",
        "scale-free networks",
        "community detection",
        "link prediction",
        "graph embedding",
        "spectral graph theory",
        "algebraic graph theory",
        "topological data analysis",
        "persistent homology",
        "Morse theory",
        "sheaf theory",
        "applied category theory",
        "topos theory",
        "non-well-founded set theory",
        "coalgebra",
        "monad",
        "comonad",
        "higher-order abstract syntax",
        "dependent types",
        "homotopy type theory",
        "univalent foundations",
        "proof-carrying code",
        "separation logic",
        "Hoare logic",
        "modal logic",
        "linear logic",
        "substructural logics",
        "paraconsistent logic",
        "relevance logic",
        "quantum logic",
        "quantum computing",
        "quantum algorithms",
    ]
    return themes


def get_styles():
    styles = [
        "historical",
        "analytical",
        "critical",
        "instructional",
    ]
    return styles


def create_prompt(t: int, q: int):
    themes = get_themes()
    styles = get_styles()
    theme = random.choices(themes, k=t)
    style = random.choice(styles)
    prompt = f"Instructions: Write `{q}` questions, theme them in any of these categories: {theme} in a {style} style."
    return prompt


class InputGenerator:
    def __init__(self) -> None:
        self.validator_settings = ValidatorSettings()  # type: ignore
        key = self.validator_settings.api_key
        self.client = OpenAI(api_key=key)  # type: ignore

    def _treat_response(self, response: ChatCompletion):
        answers: list[dict[str, str]] = []
        for msg in response.choices:

            finish_reason = msg.finish_reason
            if finish_reason != "stop":
                raise ValueError(418, finish_reason)

            content = msg.message.content
            if content:
                answers.append(json.loads(content))
        return answers

    def prompt_question_gpt(
        self, text: str, question_amount: int, model: str = "gpt-3.5-turbo"
    ):
        assistant_prompt = (
            "You output only valid JSON, in the following structure:\n"
            f'[{{"questions": ["question1", "question2", ..., "question{question_amount}"]}}]'
        )

        system_prompt = (
            f"You are an expert question generator. Your task is to create {question_amount} high-quality, relevant questions based on the given themes. "
            "Follow the guidelines and examples provided to generate questions in the specified JSON format."
        )

        response = self.client.chat.completions.create(
            model=model,
            temperature=self.validator_settings.question_temperature,
            response_format={"type": "json_object"},
            messages=[
                {
                    "role": "system",
                    "content": system_prompt,
                },
                {
                    "role": "assistant",
                    "content": assistant_prompt,
                },
                {
                    "role": "user",
                    "content": text,
                },
            ],
        )
        answers = self._treat_response(response)
        return {"Answer": answers}

    def prompt_answer_gpt(self, questions: str, model: str = "gpt-3.5-turbo"):
        response = self.client.chat.completions.create(
            model=model,
            temperature=self.validator_settings.answer_temperature,
            response_format={"type": "json_object"},
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant designed to output JSON.",
                },
                {
                    "role": "user",
                    "content": "Answer those questions, one line for each"
                    + "\n".join(questions),
                },
            ],
        )
        answers = self._treat_response(response)
        return {"Answer": answers}


if __name__ == "__main__":
    ig = InputGenerator()
    q = 2
    prompt = create_prompt(t=3, q=q)
    questions = ig.prompt_question_gpt(prompt, q)["Answer"][0]["questions"]
    # question_list = [
    #     "What is RDF (Resource Description Framework) used for in the context of web development?",
    #     "Can you explain the basic structure of an RDF statement?",
    #     "How are ontologies used in the field of artificial intelligence?",
    #     "What is the role of genetic algorithms in the field of evolutionary computation?",
    #     "How do RDF triples differ from traditional data models?",
    #     "Why is it important to define ontologies when building intelligent systems?",
    #     "In genetic algorithms, what is the purpose of the crossover operation?",
    #     "How does RDF support interoperability on the web?",
    #     "What are some popular ontology languages used for developing ontologies?",
    #     "What are the key components of a genetic algorithm?",
    #     "How do you represent knowledge in RDF?",
    #     "What are some challenges associated with designing and maintaining ontologies?",
    #     "Why are genetic algorithms well-suited for optimization problems?",
    #     "How can ontologies be leveraged for semantic web applications?",
    #     "What role does mutation play in the genetic algorithm process?",
    #     "How does RDF support data integration across different systems?",
    #     "What are some real-world applications of genetic algorithms?",
    #     "How can ontologies facilitate natural language processing tasks?",
    #     "In what ways can genetic algorithms be personalized or customized for specific problem domains?",
    #     "What are some common tools and frameworks used for working with RDF data?",
    # ]
    answers = ig.prompt_answer_gpt(questions)
    answers = answers["Answer"][0]
    for q, a in zip(questions, answers.values()):

        print(f"question: {q}")
        print(f"answer: {a}")
        print("-------------------")
