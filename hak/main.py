from fastapi import FastAPI

# from hak.config import settings

app = FastAPI(
    # title=settings.PROJECT_NAME,
    # description=settings.PROJECT_DESCRIPTION
)


@app.get("/health", include_in_schema=False)
def health_check():
    return
