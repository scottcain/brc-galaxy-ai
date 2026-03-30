import asyncio
import gxy

async def main():
    print("Testing gxy.get on collection...")
    try:
        res = await gxy.get(".*etandem on collection.*", identifier_type="regex")
        print(f"Result: {len(res)} items")
        print(res[0])
    except Exception as e:
        print(f"Error: {e}")

asyncio.run(main())
