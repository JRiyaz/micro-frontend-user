from sqlalchemy.ext.asyncio.engine import create_async_engine


class DatabaseClient:
    """Database client."""

    def __init__(self):
        """."""

        async_engine = create_async_engine(
            self.build_url(),
            isolation_level=CONFIG.DB_ISOLATION_LEVEL,
            echo=CONFIG.DB_ECHO,
            pool_recycle=CONFIG.DB_POOL_RECYCLE,
            pool_size=CONFIG.DB_POOL_SIZE,
            max_overflow=CONFIG.DB_MAX_OVERFLOW,
        )
        self.session_factory = async_scoped_session(
            sessionmaker(
                autocommit=False,
                autoflush=False,
                bind=async_engine,
                class_=AsyncSession,
                expire_on_commit=False,
            ),
            scopefunc=current_task,
        )

    @asynccontextmanager
    async def get_async_session(self) -> AsyncContextManager[AsyncSession]:
        """Prepare new session."""

        session = self.session_factory()

        try:
            yield session
        finally:
            await session.close()
