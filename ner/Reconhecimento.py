from presidio_analyzer import AnalyzerEngine, RecognizerRegistry, Pattern, PatternRecognizer
from presidio_analyzer.nlp_engine import NlpEngineProvider

class DetectorSimples:
    """Classe para criar um detector simples em português com CPF.
    
    https://microsoft.github.io/presidio/analyzer/
    https://nelsonfrugeri-tech.medium.com/domine-a-anonimiza%C3%A7%C3%A3o-de-dados-pii-para-o-desenvolvimento-de-software-3-0-d9d8e9c2e492
    """

    
    def __init__(self):
        # Configuração do spaCy PT-BR
        self.nlp_config = {
            "nlp_engine_name": "spacy",
            "models": [{"lang_code": "pt", "model_name": "pt_core_news_lg"}]
        }

        # Criar engine NLP
        self.nlp_provider = NlpEngineProvider(nlp_configuration=self.nlp_config)
        self.nlp_engine = self.nlp_provider.create_engine()

        # Criar registry e carregar reconhecedores padrão
        self.registry = RecognizerRegistry()
        self.registry.load_predefined_recognizers(nlp_engine=self.nlp_engine)

        # Adicionar reconhecedor de CPF customizado
        cpf_pattern = Pattern(
            name="CPF",
            regex=r"\b\d{3}\.?\d{3}\.?\d{3}[-\.]?\d{2}\b",
            score=0.9
        )
        cpf_recognizer = PatternRecognizer(
            supported_entity="CPF",
            patterns=[cpf_pattern],
            name="CPF Recognizer",
            supported_language="pt"
        )
        self.registry.add_recognizer(cpf_recognizer)

        # Criar analyzer final
        self.analyzer = AnalyzerEngine(registry=self.registry, nlp_engine=self.nlp_engine)

    def analyze(self, text, entities=None, language="pt"):
        """Detecta entidades no texto usando o analyzer configurado."""
        if entities is None:
            entities = ["CPF"]  # padrão: apenas CPF
        return self.analyzer.analyze(text=text, language=language, entities=entities)