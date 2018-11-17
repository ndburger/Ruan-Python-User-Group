# -*- mode: python -*-

block_cipher = None


a = Analysis(['frontend_06.py'],
             pathex=['E:\\Dropbox\\___IASTATE\\MIS407\\_F16_MIS407_repos\\Class-Notes-and-Admin\\Classes\\w08c24'],
             binaries=None,
             datas=None,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='frontend_06',
          debug=False,
          strip=False,
          upx=True,
          console=False )
