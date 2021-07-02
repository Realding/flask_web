class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    TESTING = False
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # upload file size max 16M
    JSON_AS_ASCII = False


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    TESTING = True


configs = {
    'default': Config,
    'testing': TestConfig
}
