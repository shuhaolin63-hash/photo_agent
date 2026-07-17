#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
下载其他类型摄影参考图片
- 星空摄影
- 生态摄影
- 建筑摄影
- 静物摄影

每类25张，共100张
使用 Picsum Photos 作为图片来源
"""

import os
import time
import random
import urllib.request
import urllib.error
from pathlib import Path

# 基础配置
BASE_DIR = Path("f:/aichatcut/photo_agent/reference/master_works/other_master_photos")
CATEGORIES = {
    "starry": [
        "milky-way-astro",
        "deep-space-nebula",
        "night-sky-stars",
        "star-trail-photo",
        "aurora-borealis",
    ],
    "ecology": [
        "wildlife-close-up",
        "endangered-animal",
        "underwater-marine",
        "bird-nature-photo",
        "polar-bear-arctic",
    ],
    "architecture": [
        "modern-architecture",
        "minimalist-facade",
        "urban-geometric",
        "interior-light",
        "skyscraper-city",
    ],
    "still_life": [
        "minimal-still-life",
        "food-elegant",
        "floral-dark-bg",
        "product-minimal",
        "classic-arrangement",
    ],
}

# Picsum 图片尺寸
WIDTH = 1920
HEIGHT = 1280


def download_image(url: str, save_path: Path, timeout: int = 30) -> bool:
    """下载单张图片"""
    try:
        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/120.0.0.0 Safari/537.36"
            )
        }
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=timeout) as response:
            if response.status == 200:
                data = response.read()
                if len(data) > 1024:  # 至少1KB
                    save_path.write_bytes(data)
                    return True
    except Exception as e:
        print(f"  下载失败: {e}")
    return False


def main():
    print("=" * 60)
    print("开始下载其他类型摄影参考图片")
    print("=" * 60)

    total_downloaded = 0
    total_failed = 0

    for category, keywords in CATEGORIES.items():
        cat_dir = BASE_DIR / category
        cat_dir.mkdir(parents=True, exist_ok=True)

        print(f"\n【{category}】下载到: {cat_dir}")
        print("-" * 40)

        category_downloaded = 0
        category_failed = 0
        file_index = 1

        for keyword in keywords:
            for i in range(5):  # 每个关键词5张
                # 使用不同的 seed 确保图片不同
                seed = f"{keyword}-{i}-{random.randint(1000, 9999)}"
                url = f"https://picsum.photos/seed/{seed}/{WIDTH}/{HEIGHT}"

                filename = f"{category}_{file_index:02d}.jpg"
                save_path = cat_dir / filename

                # 如果文件已存在则跳过
                if save_path.exists():
                    print(f"  跳过(已存在): {filename}")
                    file_index += 1
                    category_downloaded += 1
                    total_downloaded += 1
                    continue

                print(f"  下载: {filename} <- seed={seed}")
                success = download_image(url, save_path)

                if success:
                    category_downloaded += 1
                    total_downloaded += 1
                else:
                    category_failed += 1
                    total_failed += 1

                file_index += 1
                time.sleep(0.5)  #  polite delay

        print(f"  类别完成: 成功 {category_downloaded} 张, 失败 {category_failed} 张")

    print("\n" + "=" * 60)
    print(f"总计: 成功 {total_downloaded} 张, 失败 {total_failed} 张")
    print("=" * 60)


if __name__ == "__main__":
    main()
