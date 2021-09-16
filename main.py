import argparse
import logging

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='[Autoplayer] auto windows player using pyautogui')
    parser.add_argument('--game', type=str, required=True, default="碧蓝航线", help="game that want to use")
    parser.add_argument('--task', type=str, required=True, help="auto task, see readme for detail")
    parser.add_argument('--times', type=int, required=True, default=1, help="running times for auto task")
    args = parser.parse_args()
    print(f"Autoplayer start with parameter: game/{args.game}, task/{args.task}, times/{args.times}")
