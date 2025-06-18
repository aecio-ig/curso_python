# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['topicos\\M05_PySide6\\A04_Calculadora\\main.py'],
    pathex=[],
    binaries=[],
    datas=[('topicos\\M05_PySide6\\A04_Calculadora\\files', 'files')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='Calculadora',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['topicos\\M05_PySide6\\A04_Calculadora\\files\\icon.png'],
)
