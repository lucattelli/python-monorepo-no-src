import asyncio

from ai_pipeline.pipeline import run_pipeline


async def main() -> None:
    await run_pipeline()



if __name__ == '__main__':
    asyncio.run(main())
