阶段 0：本周任务卡（W00-W01：把环境变成"能出活"的状态）
阶段目标：W01 结束时，你的 GitHub 上有一个能跑、能看、能讲的 mini 语言模型（哪怕很弱）。 不再有"打基础"这个阶段。代码是项目的副产品，每天只在收尾时花 20-30 分钟。

🔵 里程碑 M0（不看日期，达成才进阶段 1）
GitHub 上有 learn---log 仓库，且能证明是你在提交（git log 里是你的名字）
本地有 ~/learn、~/projects、~/notes 三个目录
Colab 上跑通过一次 Python，且能在 T4 GPU 上跑通一次 PyTorch 训练
拿到至少 1 个可用的模型推理入口（免费 API 或本地模型二选一，见 W00D3）
仓库里有 1 个别人照着 README 能跑起来的代码文件
🏗️ W00D1｜11-19 周四｜把 Git 身份配好、仓库确认能推（0.5h）
目标：今天结束时，你后面 12 周的每一次提交都算在你名下。

打开什么	终端
做什么	运行下面 4 行
验收	git config --global --list 能看到 4 项；GitHub 网页能看到你的仓库
卡住	报 not in a git directory → cd ~/learn/learn-log 再执行
git config --global user.name "jdoawjdn"
git config --global user.email "ljl780221041@outlook.com"
git config --global credential.helper osxkeychain
git config --global init.defaultBranch main
git config --global --list
常见坑

邮箱要和 GitHub 账号一致，否则贡献图不算你的（功能不受影响，但简历上难看）
只配 user.email 不配 user.name → commit 会显示奇怪的名字
配完以后新提交才算数，之前的 5 个 uia 提交改不了，别去改
今日收尾：cd ~/learn/learn-log && ~/learn/d.sh "chore: 配置 git 身份"

🏗️ W00D2｜11-20 周五｜建目录、跑通第一个项目骨架（1h）
目标：有一个"项目的"标准目录，后面 12 周所有代码都往里放。

打开什么	终端 + VS Code
做什么	建目录 → 建 ~/projects/mini-gpt 骨架 → 跑通 python3 main.py 输出 "hello"
验收	python3 main.py 输出 hello mini-gpt；~/learn/d.sh 推送成功
卡住	command not found: code → 打开 VS Code → Cmd+Shift+P → 输入 Shell Command: Install 'code' command in PATH
常见坑	① 目录名带空格 → 别带；② 文件保存成 main.py.txt → VS Code 右下角看语言是不是 Python
mkdir -p ~/learn ~/projects ~/notes
cd ~/projects
mkdir -p mini-gpt && cd mini-gpt
git init -b main
cat > main.py <<'EOF'
def main():
    print("hello mini-gpt")

if __name__ == "__main__":
    main()
EOF
python3 main.py
🔵 W00D3｜11-21 周六｜拿到可用的模型推理入口（2h）★关键
目标：今天结束时，你能在代码里调用一个大模型。这是后面所有项目的燃料。 两条路，选一条。选好后在卡点日志里写"我选了 A/B"。

路线 A：免费 API（推荐，最快 30 分钟出结果）
平台	地址	免费额度	注册要点
硅基流动 SiliconFlow	https://cloud.siliconflow.cn	注册送 14 元额度，含 Qwen/DeepSeek 等	手机号注册，实名后可用
DeepSeek 开放平台	https://platform.deepseek.com	新用户有赠送额度	手机号注册
智谱 BigModel	https://open.bigmodel.cn	新用户赠送 tokens	手机号注册
拿到 key 后，直接跑这个（把 sk-xxx 换成你的 key，base_url 换成对应平台的）：

pip install openai -i https://pypi.tuna.tsinghua.edu.cn/simple
python3 - <<'EOF'
from openai import OpenAI
client = OpenAI(api_key="sk-xxx", base_url="https://api.siliconflow.cn/v1")
r = client.chat.completions.create(
    model="Qwen/Qwen2.5-7B-Instruct",
    messages=[{"role": "user", "content": "用一句话解释什么是 attention"}],
)
print(r.choices[0].message.content)
EOF
验收：终端打印出一句中文回答。

路线 B：本地小模型（不花钱，但慢，适合练"部署"）
⚠️ 注意：你的 Mac 是 Apple 芯片，本机跑不了 CUDA 版 PyTorch，要走 MPS 或 CPU。7B 模型在 M 系列上能跑，但很慢。 所以本地路线只用于"跑通一次推理"，训练一律去 Colab。

pip install mlx-lm -i https://pypi.tuna.tsinghua.edu.cn/simple
# 模型从国内镜像下（HuggingFace 国内直连经常失败，用 hf-mirror）
export HF_ENDPOINT=https://hf-mirror.com
mlx_lm.generate --model Qwen/Qwen2.5-0.5B-Instruct --prompt "你好" --max-tokens 50
验收：终端打印出一段回答。

卡住时的排查顺序
AuthenticationError → key 抄错了或没复制全
ConnectionError / 超时 → 换手机热点；或检查 base_url 尾部有没有 /v1
model not found → 模型名要和平台完全一致（大小写都算），去平台文档复制
本地下载卡在 0% → 确认 HF_ENDPOINT=https://hf-mirror.com 已 export
🚀 W00D4｜11-22 周日｜第一个项目：调 API 写一个"提示词对比实验"（2.5h）
目标：这是你的第一个可展示产出。证明"我能调模型，而且会做实验"。

打开什么	~/projects/prompt-lab/
做什么	用同一个问题，跑 3 种不同系统提示词，保存 3 份输出到 JSON，写一个对比结论
验收	仓库里有一个 results.json 和 README 里一段"哪种提示词更好，为什么（用具体例子说）"
卡住	json.dump 中文变 \u4e2d → 加参数 ensure_ascii=False
常见坑	① 把 key 直接写进代码并 push → 绝对不要，用环境变量，见下方
mkdir -p ~/projects/prompt-lab && cd ~/projects/prompt-lab
git init -b main
printf '.env\n__pycache__/\n' > .gitignore
# experiment.py
import json, os
from openai import OpenAI

client = OpenAI(api_key=os.environ["API_KEY"],      # 从环境变量读，不写死在代码里
                base_url="https://api.siliconflow.cn/v1")

QUESTION = "一个刚学编程的研究生，想 3 个月后拿到大模型实习，第一周该做什么？"
PROMPTS = {
    "v1_无角色": QUESTION,
    "v2_专家角色": "你是一位带过多届实习生的算法团队负责人。" + QUESTION,
    "v3_结构化": "你是一位算法团队负责人。请按 目标/本周动作/验收标准 三部分回答，每部分不超过 3 条。\n" + QUESTION,
}
results = {}
for name, p in PROMPTS.items():
    r = client.chat.completions.create(
        model="Qwen/Qwen2.5-7B-Instruct",
        messages=[{"role": "user", "content": p}], temperature=0.3)
    results[name] = r.choices[0].message.content

with open("results.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)
print("已保存 results.json")
运行	export API_KEY="sk-xxx" 然后 python3 experiment.py
提交	~/learn/d.sh "feat: 第一个项目 prompt-lab，3 组提示词对比"
README 要写	一段"结论"：哪种提示词好、好在哪里、举一句原文对比
🚀 W00D5｜11-23 周一｜把 prompt-lab 做成"能给别人看"的样子（2h）
做什么	① 生成 20 个测试问题（自己编，覆盖不同难度）；② 加一个 run_all.py 一次跑完并输出成 Markdown 表格；③ 写 README
验收	别人 clone 下来，设好 key，一条命令出结果
常见坑	一次性调用 20 次会触发限流 → 加 time.sleep(1)
README 模板（直接抄，改内容）：

# prompt-lab
对比 3 种提示词策略在 XX 类任务上的效果。

## 运行
export API_KEY=你的key
pip install -r requirements.txt
python3 run_all.py

## 结果
| 策略 | 格式遵守率 | 平均字数 | 主观评分 |
|---|---|---|---|
| v1 | 4/20 | 210 | 2.8 |
| v2 | 9/20 | 260 | 3.4 |
| v3 | 18/20 | 190 | 4.1 |

## 结论
结构化提示词在"格式遵守"上几乎必赢（18/20 vs 4/20），代价是字数减少、灵活性下降。
适合需要稳定输出的批量任务，不适合开放式创意。
这是一个"软交付"📦，但它是你第一个能让面试官问"你怎么评的"的项目。

🔵 W00D6｜11-24 周二｜GitHub Pages 或最简单的图片展示（1h）｜可选
如果你想让简历上有一个能点开的链接。

做什么	在 prompt-lab 仓库 → Settings → Pages → 选 main 分支 → 得到一个 https://jdoawjdn.github.io/prompt-lab/
验收	打开链接能看到 README 渲染的页面
卡住	Pages 要 1-5 分钟才生效，别以为失败了
每周固定节奏（从本周开始，以后每周都这样）
天	角色
D1	环境/准备（如果上周遗留了基建问题，放这天）
D2	主线项目 · 第一块
D3	主线项目 · 第二块
D4	主线项目 · 第三块 + 首次跑通
D5	整合 + README + 复盘
D6（周六）	补漏 + 下周预习（4-5h）
D7（周日）	休息
📝 本周复盘卡（W00 结束时填，5 分钟）
这周我做出来的东西是什么？（贴链接）
卡最久的那个问题是什么？怎么解决的？
下周我最想搞懂的一件事是什么？
📌 关于代码基础那点事的处理（不要删，以后每周都会用到）
每天收尾 20-30 分钟，从今天开始，按这个顺序做，做完就停：

时间	做什么
每天 10 分钟	在 ~/learn/learn-log 里做 1 道 LeetCode 热题简单题（https://leetcode.cn/studyplan/top-100-liked/ 按标签点）
每周 1 次 20 分钟	做 ex_w00d3.py/ex_w00d4.py 里的 1-2 题（已在你仓库里，带测试）
你写 sum = sum(xs) 那个 bug，是初学者最经典的"变量名覆盖内置函数"。正确写法：

def mean(xs):
    if not xs:
        return None
    total = sum(xs)      # 变量名换成 total
    return total / len(xs)
报错 UnboundLocalError: cannot access local variable 'sum' 的意思是：函数内部只要给 sum 赋过值，Python 就认为整个函数里的 sum 都是局部变量，所以第一行 sum(xs) 时它还不存在。

这个知识点，比"学完 Python 基础语法"重要一百倍。 你现在知道它，比刷 100 道 A+B 有用。