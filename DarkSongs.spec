# -*- mode: python ; coding: utf-8 -*-


from PyInstaller.config import CONF


block_cipher = None


a = Analysis(
    ['DarkSongs.py'],
    pathex=[],
    binaries=[],
    datas=[('Python/Lib/site-packages/customtkinter', 'customtkinter/'),
            ('Python/Lib/site-packages/librosa', 'librosa/'),
            ('Python/Lib/site-packages/sklearn', 'sklearn/'),
            ('Python/Lib/site-packages/vgamepad', 'vgamepad/')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
files = [('Actions.json', 'Actions.json', 'DATA'),
        ('Tones.json', 'Tones.json', 'DATA'),
        ('Configuration.json', 'Configuration.json', 'DATA'),
        ('Image.png', 'Image.png', 'DATA'),
        ('Icon.ico', 'Icon.ico', 'DATA'),
        ('Strings.wav', 'Strings.wav', 'DATA')]

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

CONF['distpath'] = "build"
exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    name='DarkSongs',
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
    contents_directory='.',
    icon=['Icon.ico'],
)

CONF['distpath'] = "dist"
coll = COLLECT(
    exe,
    files,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='DarkSongs',
)
