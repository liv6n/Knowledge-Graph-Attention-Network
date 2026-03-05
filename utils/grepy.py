import numpy as np

# 1. 加载推荐结果文件（替换为你的实际路径）
rec_path = r"C:\Users\oybl\OneDrive\桌面\KGAT-pytorch-master\KGAT-pytorch-master\trained_model\ECFKG\amazon-book\embed-dim64_lr0.005_pretrain1\cf_scores.npy"
top_k_recs = np.load(rec_path, allow_pickle=True).item()

# 2. 自定义查看的用户ID和Top-K值
target_user_id = 0  # 查看第0个用户的推荐结果
top_k = 10          # 提取Top-10推荐

# 3. 输出结果
if target_user_id in top_k_recs:
    top_items = top_k_recs[target_user_id][:top_k]
    print(f"✅ 用户{target_user_id}的Top-{top_k}推荐物品ID：")
    print(top_items)
else:
    print(f"❌ 未找到用户{target_user_id}的推荐结果")

# 4. 可选：统计所有用户的推荐覆盖度（看推荐的多样性）
all_recommended_items = set()
# 统计前100个用户的Top-10推荐物品
for user_id in list(top_k_recs.keys())[:100]:
    all_recommended_items.update(top_k_recs[user_id][:10])
print(f"\n📊 前100个用户Top-10推荐覆盖的物品总数：{len(all_recommended_items)}")