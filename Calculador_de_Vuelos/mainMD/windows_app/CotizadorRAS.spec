# -*- mode: python ; coding: utf-8 -*-

import sys
import os

from kivy_deps import sdl2, glew

from kivymd import hooks_path as kivymd_hooks_path

block_cipher = None


a = Analysis(['D:\\Documents\\Robotic Air Systems\\Cotizador\\Calculador_de_Vuelos\\mainMD\\main.py'],
             pathex=['D:\\Documents\\Robotic Air Systems\\Cotizador\\Calculador_de_Vuelos\\mainMD\\windows_app'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[kivymd_hooks_path],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='CotizadorRAS',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False , icon='D:\\Documents\\Robotic Air Systems\\Cotizador\\Calculador_de_Vuelos\\mainMD\\mpdesktop.ico')
coll = COLLECT(exe,Tree('D:\\Documents\\Robotic Air Systems\\Cotizador\\Calculador_de_Vuelos\\mainMD\\'),
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
               upx=True,
               upx_exclude=[],
               name='Cotizador RAS')
