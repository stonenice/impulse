import { Component,ForwardRefExoticComponent } from 'react'
import { connect } from 'umi'
import styles from './index.less'

import { 
  MessageOutlined,
  RedditOutlined,
  NodeIndexOutlined,
  SlackOutlined
} from '@ant-design/icons'

import {
  Toast,
  Badge,
  WhiteSpace,
  Grid
} from 'antd-mobile'


class HomePage extends Component<any, any> {
  constructor(props: any) {
    super(props);
    console.log(props);

    //bind this for function
    this.onEntranceItemClick=this.onEntranceItemClick.bind(this);
  }

  changeAuthor() {
    const { dispatch } = this.props;
    dispatch({
      type: 'home/changeAuthor',
      payload: 'mytest'
    });
  }

  getIconByCode(code:string):any{
    const iconCodeMap:Map<string,any>=new Map([
      ['primary_school',RedditOutlined],
      ['primary_to_middle',NodeIndexOutlined],
      ['school_house',SlackOutlined]
    ]);
    return iconCodeMap.get(code);
  }

  onEntranceItemClick(code:string):void{
    console.log('onEntranceItemClick:',code);
    Toast.offline('功能尚未开通，敬请期待...');
  }

  render() {
    const { 
      entranceList,
      areaListOfCity  
    } = this.props;
  
    return (
      <div>
        <div className={styles.app_header_bg}></div>
        <div className={styles.home_page_container}>
          <div className={styles.app_top_bar}>
            <div>
              <div style={{ display: 'inline-block', float: 'left', color: 'white' }}><span>成都市</span></div>
              <div style={{ display: 'inline-block', float: 'right', color: 'white'}}>
                <MessageOutlined style={{ fontSize: '18px' }} />&nbsp;
                <span>消息通知</span>
                <Badge text={100} overflowCount={99} style={{marginTop:-20}}/>
              </div>
            </div>
            <div style={{ clear: 'both' }}></div>
          </div>
          <div className={styles.app_nav_guard}>
            <Grid data={entranceList} hasLine={false} columnNum={3}
                renderItem={item=>{
                  const EntranceIcon=this.getIconByCode(item?.code)
                  return (
                      <div className={styles.app_entrance_block} onClick={()=>{this.onEntranceItemClick(item?.code);}}>
                        <div style={{height:45,padding:'10px 5px 0px 5px'}}><EntranceIcon style={{ fontSize:32}} /></div>
                        <span>{item?.name}</span>
                      </div>
                  )}
              }/>
          </div>
          <WhiteSpace/>
          <div className='list-filter-area'>
            <div className={styles.list_filter_row}>
              <div className={styles.list_filter_label}>区域</div>
              <div style={{justifyContent:'flex-end',flex:1,overflow:'scroll',whiteSpace:'nowrap'}}>{areaListOfCity.map((x:any)=>(<div key={x.name} className={styles.list_filter_block}>{x.name}</div>))}</div>
            </div>
            <div className={styles.list_filter_row}>
              <div className={styles.list_filter_label}>学段</div>
              <div style={{justifyContent:'flex-end',flex:1,overflow:'scroll',whiteSpace:'nowrap'}}>
                <div className={styles.list_filter_block}>幼儿园</div>
                <div className={styles.list_filter_block}>小学</div>
                <div className={styles.list_filter_block}>初中</div>
                <div className={styles.list_filter_block}>高中</div>
            </div>
            </div>
            <div className={styles.list_filter_row}>
              <div className={styles.list_filter_label}>性质</div>
              <div style={{justifyContent:'flex-end',flex:1,overflow:'scroll',whiteSpace:'nowrap'}}>
                <div className={styles.list_filter_block}>公办</div>
                <div className={styles.list_filter_block}>民办</div>
            </div>
            </div>
      
          </div>
          <div className='list-table'>
          </div>
        </div>
      </div>
    )
  }
}

//Export And mapStateToProps
export default connect((model: any) => ({ ...model['home'] }))(HomePage)
