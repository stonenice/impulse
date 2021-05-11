import { Component } from 'react';
import { connect } from 'umi';
import styles from './index.less';
import { 
  Button, 
  Carousel,
  Flex 
} from 'antd-mobile';

class HomePage extends Component<any, any> {
  constructor(props: any) {
    super(props);
    console.log(props);
  }

  changeAuthor() {
    const { dispatch } = this.props;
    dispatch({
      type: 'home/changeAuthor',
      payload: 'mytest'
    });
  }

  render() {
    const { author } = this.props;
    return (
      <div>
        <div>
        <Carousel
          autoplay={true}
          infinite
        >
            <a
                style={{ display: 'inline-block', width: '100%', height:'auto' }}>
              <img src={'/images/banner-1.jpg'}
                style={{ width: '100%',height:250, verticalAlign: 'top' }}
                onLoad={() => {window.dispatchEvent(new Event('resize'));}}/>
            </a>
            <a 
                style={{ display: 'inline-block', width: '100%', height:'auto' }}>
              <img src={'/images/banner-2.jpg'}
                style={{ width: '100%',height:250,verticalAlign: 'top' }}
                onLoad={() => {window.dispatchEvent(new Event('resize'));}}/>
            </a>
        </Carousel>
        </div>
        <div>
          <Flex>
            <Flex.Item>成都小学划片</Flex.Item>
            <Flex.Item>成都小升初</Flex.Item>
          </Flex>
        </div>
        <p>Author:{author}</p>
        <Button onClick={this.changeAuthor.bind(this)}>Test</Button>
      </div>
    );
  }
}

//Export And mapStateToProps
export default connect((model: any) => ({ ...model['home'] }))(HomePage)
