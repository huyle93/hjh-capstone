import React, {Component} from 'react';
import {Doughnut, Radar, Bar} from 'react-chartjs-2';
import {Grid, Row, Col, Table} from 'react-bootstrap';


import {Card} from 'components/Card/Card.jsx';
import {StatsCard} from 'components/StatsCard/StatsCard.jsx';
import {Tasks} from 'components/Tasks/Tasks.jsx';
import {thArray, tdArray} from 'variables/Tables.jsx';
import {iconsArray} from 'variables/Icons.jsx';

import {
    dataRadar,
    radarOptions,
    dataPie,
    pieOptions,
    dataBar,
    optionsBar,
    legendBar
} from 'variables/Charts.jsx';
import TableList from '../TableList/TableList';

class Dashboard extends Component {
    createLegend(json) {
        var legend = [];
        for (var i = 0; i < json.names.length; i++) {
            var type = `fa fa-circle text-${json.types[i]}`;
            legend.push(
                <i className={type} key={i}></i>
            );
            legend.push(' ');
            legend.push(
                json.names[i]
            );
        }
        return legend;
    }
    render() {
        return (
            <div className="content">
                <Grid fluid>
                    <Row>
                        <Col lg={3}/>
                    </Row>
                    <Row>
                        <Col lg={4} sm={6}>
                            <StatsCard
                                bigIcon={<i className="pe-7s-user text-warning"></i>}
                                statsText="Recommended Attorney"
                                statsValue="Paul S. Gillies"
                                statsIcon={<i className="fa fa-refresh"></i>}
                                statsIconText="Updated now"
                            />
                        </Col>
                        <Col lg={3} sm={6}>
                            <StatsCard
                                bigIcon={<i className="pe-7s-hammer text-success"></i>}
                                statsText="Winning Chance before all Judges "
                                statsValue="83%"
                                statsIcon={<i className="fa fa-calendar-o"></i>}
                                statsIconText="Last day"
                            />
                        </Col>
                        <Col lg={5} sm={6}>
                            <StatsCard
                                bigIcon={<i className="pe-7s-medal text-danger"></i>}
                                statsText="Winning Chance before Judge Thomas Durkin"
                                statsValue="92%"
                                statsIcon={<i className="fa fa-clock-o"></i>}
                                statsIconText="In the last hour"
                            />
                        </Col>
                    </Row>
                    <Row>
                        <Col md={7}>
                            <Card
                                id="chartActivity"
                                title="Top 10 Attorneys"
                                category="Attorney againt before Thomas Durkin"
                                stats="Updated 2 minutes ago"
                                statsIcon="fa fa-check"
                                content={
                                    <div className="ct-chart">
                                        <Bar
                                            data={dataBar}
                                            options={optionsBar}
                                        />
                                    </div>
                                }
                                legend={
                                    <div className="legend">
                                        {this.createLegend(legendBar)}
                                    </div>
                                }
                            />
                        </Col>
                        <Col md={5}>
                            <Card
                            statsIcon="fa fa-history"
                            id="chartHours"
                            title="Top Two Attorneys"
                            category="Data since 2000"
                            stats="Updated 2 minutes ago"
                            legend={
                                <div className="legend">
                                    {this.createLegend(legendBar)}
                                </div>
                            }
                   content={
                                <div id="chartPreferences" className="ct-chart">
                                    <Radar className="chart-container" data={dataRadar} options={pieOptions} />
                                </div>
                            }
                            />
                        </Col>
                    </Row>

                    <Row>
                        <Col md={7}>
                            <Card
                            statsIcon="fa fa-hourglass-2"
                            title="Similar Attorney"
                            category="Compare to Recommended Attorney "
                            stats="Updated a week ago"
                            content={
                                <Table table striped hover>
                                    <div className="tbl-header">
                                        <thead>
                                            <tr>
                                                {
                                                    thArray.map((prop, key) => {
                                                        return (
                                                        <th key={key}>{prop}</th>
                                                        );
                                                    })
                                                }
                                            </tr>
                                        </thead>
                                    </div>
                                    <div className="tbl-body">
                                        <tbody>
                                            {
                                                tdArray.map((prop, key) => {
                                                    return (
                                                        <tr key={key}>{
                                                            prop.map((prop,key) => {
                                                                return (
                                                                    <td key={key}>{prop}</td>
                                                                );
                                                            })
                                                        }</tr>
                                                    );
                                                })
                                            }
                                        </tbody>
                                    </div>
                                </Table>
                            }
                            />
                        </Col>
                        <Col md={5}>
                            <Card
                            statsIcon="fa fa-clock-o"
                            title="Probability Distribution"
                            category="Paul S. Gillies"
                            stats="Updated 2 minutes ago"
                            content={
                                <div id="chartPreferences" className="ct-chart ct-perfect-fourth">
                                    <Doughnut className="chart-container" data={dataPie} options={pieOptions} />
                                </div>
                            }
                            />
                        </Col>
                    </Row>

                </Grid>
            </div>
        );
    }
}

export default Dashboard;
