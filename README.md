# Network Automation Portfolio (Work in Progress)

このリポジトリは、Python / Ansible / RESTCONF を用いて  
ネットワーク機器の設定取得・自動化を行うポートフォリオです。

現在はネットワーク自動化スキルを可視化するために  
Python と GitHub を中心に構築中です。（WIP）

---

## 🔧 現在の進捗状況

- [x] Python 開発環境構築（VSCode / Python3.10）
- [x] GitHub リポジトリ作成
- [x] Git / VSCode 連携
- [ ] show コマンド自動取得（Netmiko）
- [ ] Config バックアップ自動化（Netmiko）
- [ ] RESTCONF GET（インターフェース情報取得）
- [ ] RESTCONF PUT（Loopback 作成）
- [ ] Ansible Playbook（構成バックアップ / VLAN / OSPF）
- [ ] README 仕上げ（完成版）

---

## 📁 フォルダ構成
network-automation-portfolio/
├── python/ # Netmiko を使った CLI 自動化
├── api/ # RESTCONF / API 自動化（予定）
├── ansible/ # Ansible Playbook（予定）
└── README.md


---

## 🛠 使用技術（予定含む）

- Python 3.10
- Netmiko（SSH自動化）
- Requests（REST API）
- Ansible（構成管理）
- YAML / Jinja2
- Git / GitHub

---

## 🚀 これから追加する自動化内容

### ✔ Python（Netmiko）
- show コマンド取得  
- Config バックアップ  
- VLAN / Loopback / OSPF の自動投入  

### ✔ RESTCONF / API
- GET：インターフェース情報取得  
- PUT：Loopback インターフェース作成  
- Postman 連携  

### ✔ Ansible
- config バックアップ  
- VLAN 追加  
- Loopback/OSPF 作成（Jinja2 テンプレ使用）  

---

## 📌 目的

- ネットワーク自動化の基礎〜応用スキルを証明
- Python・API・Ansible を扱えることを可視化
- 自動化エンジニアとしての実務レベルを示す

---

（WIP: 現在ポートフォリオ構築中）
