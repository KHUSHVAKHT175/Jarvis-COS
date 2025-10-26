# Jarvis-COS Minimal
�������쭠� ����� Jarvis COS ��� CPU + 8GB RAM.
## ?? Quick Start

```bash
# 1. �����஢���� ९������
git clone https://github.com/username/Jarvis-COS-Minimal.git
cd Jarvis-COS-Minimal

# 2. ��⠭���� ����ᨬ��⥩
pip install -r requirements.txt

# 3. ����� �᭮���� �ணࠬ��
python src/main.py

# 4. �ਬ�� ������ � ���᮫�
Jarvis-COS> chat
Jarvis-COS> schedule
Jarvis-COS> think
Jarvis-COS> status
Jarvis-COS> exit
## ?? �᭮��� 䠩�� � �����祭��

| ���� / ���� | �����祭�� |
|--------------|-------------|
| `src/main.py` | ��窠 �室�. ��ࠢ��� ����ﬨ Dialog, Scheduler, Logic. |
| `src/core/memory_engine.py` | �࠭���� � ��ࠡ�⪠ ������ �����. |
| `src/core/process_core.py` | ��ࠢ����� ����ᠬ� � ��⮪��� ��⥬�. |
| `src/core/command_parser.py` | ������ ���짮��⥫�᪨� ������. |
| `src/core/scheduler.py` | ������ �����஢騪 �����. |
| `src/core/security_shell.py` | ������᭮��� � ����஫� �ᯮ������. |
| `src/core/system_log.py` | ����஢���� ����⢨� � �訡��. |
| `src/modules/dialog/dialog.py` | ����� ������� � ����������⢨� � ���짮��⥫��. |
| `src/modules/logic/logic.py` | ����� �����᪮�� ��諥��� (I1/I2). |
| `src/modules/magic_field.py` | ����⨢�� ����� "Magic Field" (7D-�ࠪ⨪�). |
| `src/modules/vision/vision_adapter.py` | ���㠫쭠� �����⥬� / ������ �������. |
| `src/modules/scheduler/scheduler.py` | �����஢騪 ����� ���孥�� �஢��. |
| `src/modules/intuition/intuition_layer.py` | ����� ����⨢���� ᫮�. |
| `tests/test_core.py` | ����� ��⮢ ��� �஢�ન �� � ������. |
```bash
# ����� ��⮢
pytest
�������� १����:
� ���᮫� ������� ��ப� � �ᯥ�� ��宦������ ��⮢ (test passed), �� ���⢥ত��� ���४⭮��� ࠡ��� �� � ���㫥�.
```markdown
## ? FAQ

**��� �������� ���� �����?**  
������� ����� � `src/modules/`, ������� ᢮� 䠩� `new_module.py` � ����ᮬ `NewModule`, ��ॣ������� ��� � `src/main.py` � ᫮��� `modules`.

**��� ᤥ���� pull-request?**  
1. ������� �� ९������.  
2. ������� ����: `git checkout -b feature/my-feature`.  
3. ����� ��������� � �믮���� ������.  
4. ��ࠢ�� Pull Request � ���ᠭ��� ���������.

**�㤠 ����� ���� � �।�������?**  
�ᯮ���� ������� **Issues** �� GitHub-��࠭�� �஥�� ��� ��ࠢ�� ���쬮 �� ����, 㪠����� � ࠧ���� "Contacts" README.md.
