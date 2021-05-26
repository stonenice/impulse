import { defineConfig } from 'umi'
import fs from 'fs'
import path from 'path'

export default defineConfig({
  title:'xasync.com',
  favicon: '/favicon.ico',
  publicPath:'/',
  nodeModulesTransform: {
    type: 'none',
  },
  fastRefresh: {},
  theme:{
    appMainColor:'#087db4'
  }
});
