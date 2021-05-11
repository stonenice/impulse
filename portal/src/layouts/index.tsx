import { connect,history } from 'umi'
import { Component } from 'react'
import {trim} from 'lodash'
import { TabBar } from 'antd-mobile'
import { HomeOutlined, UserOutlined, DashboardOutlined } from '@ant-design/icons'

class Layout extends Component<any, any>{
  constructor(props: any) {
    super(props);
    let pathList=trim(props.location.pathname,'/').split('/')
    let reqTab=(pathList&&pathList.length>0)?pathList[0]:'home';
    if(reqTab!=props.currentActiveTab){
      this.onPressTab(reqTab);
    }
    this.onPressTab=this.onPressTab.bind(this);
  }

  onPressTab(tabKey: string) {
    const { dispatch } = this.props;
    console.log('onPressTab:',tabKey)
    dispatch({
      type: 'system/changeAppTag',
      payload: tabKey
    })
    history.push('/'+tabKey)
  }

  render() {
    const {
      children,
      currentActiveTab
    } = this.props;

    return (
      <div style={{ position: 'fixed', height: '100%', width: '100%', top: 0 }}>
        <TabBar
          unselectedTintColor="#949494"
          tintColor="#33A3F4"
          barTintColor="white">
          <TabBar.Item title="首页" key="home" selected={currentActiveTab == 'home'}
            icon={<HomeOutlined style={{ fontSize: 25 }} />}
            selectedIcon={<HomeOutlined style={{ fontSize: 25, backgroundColor: 'eb2f96' }} />}
            onPress={()=>this.onPressTab('home')}
          >
            {children}
          </TabBar.Item>

          <TabBar.Item title="效率" key="work" selected={currentActiveTab == 'work'}
            icon={<DashboardOutlined style={{ fontSize: 25 }} />}
            selectedIcon={<DashboardOutlined style={{ fontSize: 25, backgroundColor: 'eb2f96' }} />}
            onPress={()=>this.onPressTab('work')}
          >
            {children}
          </TabBar.Item>

          <TabBar.Item title="我的" key="mine" selected={currentActiveTab == 'mine'}
            icon={<UserOutlined style={{ fontSize: 25 }} />}
            selectedIcon={<UserOutlined style={{ fontSize: 25, backgroundColor: 'eb2f96' }} />}
            onPress={()=>this.onPressTab('mine')}
          >
            {children}
          </TabBar.Item>
        </TabBar>
      </div>
    );
  }
}

export default connect((model: any) => ({ ...model['system'] }))(Layout)