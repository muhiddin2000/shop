from modeltranslation.fields import TranslationField


class CategoryTranslation(TranslationField):
    fields = ('name')
    required_languages = ('en')
