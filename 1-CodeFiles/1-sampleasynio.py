import asyncio
import time

async def prepare_coffee():
    print('preparing cofee')
    await asyncio.sleep(2)
    print('coffee completed')

async def prepare_baggle():
    print('preparing baggle')
    await asyncio.sleep(3)
    print('baggle completed')

async def main():
    start= time.time()
    await asyncio.gather(prepare_baggle() , prepare_coffee() )   ## bhai agey nhi badna tab tak ye pura funsih na ho jaye 
    end =time.time()
    print(f'total time {end-start}')




asyncio.run(main())
