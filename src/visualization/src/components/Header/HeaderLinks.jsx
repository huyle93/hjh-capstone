import React, {Component} from 'react';
import { NavItem, Nav, NavDropdown, MenuItem } from 'react-bootstrap';
import Autosuggest from 'react-autosuggest';

// Imagine you have a list of languages that you'd like to autosuggest.
const languages = [
    {
        name: 'Thomas Durkin'
    },
    {
        name: 'John Zaikowski'
    },
    {
        name: 'Tony Adam'
    },
  ];
// Teach Autosuggest how to calculate suggestions for any given input value.
const getSuggestions = value => {
    const inputValue = value.trim().toLowerCase();
    const inputLength = inputValue.length;
  
    return inputLength === 0 ? [] : languages.filter(lang =>
      lang.name.toLowerCase().slice(0, inputLength) === inputValue
    );
  };
  
// When suggestion is clicked, Autosuggest needs to populate the input
// based on the clicked suggestion. Teach Autosuggest how to calculate the
// input value for every given suggestion.
const getSuggestionValue = suggestion => suggestion.name;

// Use your imagination to render suggestions.
const renderSuggestion = suggestion => (
    <div>
        {suggestion.name}
    </div>
);

class HeaderLinks extends Component{
    constructor() {
        super();

        // Autosuggest is a controlled component.
        // This means that you need to provide an input value
        // and an onChange handler that updates this value (see below).
        // Suggestions also need to be provided to the Autosuggest,
        // and they are initially empty because the Autosuggest is closed.
        this.state = {
            value: '',
            suggestions: []
        };
    }

    onChange = (event, { newValue }) => {
        this.setState({
            value: newValue
        });
    };

    // Autosuggest will call this function every time you need to update suggestions.
    // You already implemented this logic above, so just use it.
    onSuggestionsFetchRequested = ({ value }) => {
        this.setState({
            suggestions: getSuggestions(value)
        });
    };

    // Autosuggest will call this function every time you need to clear suggestions.
    onSuggestionsClearRequested = () => {
        this.setState({
            suggestions: []
        });
    };

    // Test to see if click the page it would load
    onSuggestionSelected = (event, { languages, suggestionValue, suggestionIndex, sectionIndex, method }) =>{
    }
    // Render Component
    render(){
        const { value, suggestions } = this.state;

        // Autosuggest will pass through all these props to the input.
        const inputProps = {
            placeholder: 'Judges name',
            value,
            onChange: this.onChange,

            
        };
        const notification = (
            <div>
                <i className="fa fa-globe"></i>
                <b className="caret"></b>
                <span className="notification">5</span>
                <p className="hidden-lg hidden-md">Notification</p>
            </div>
        );
        return (
            <div>
                <Nav>
                    <NavItem eventKey={1} href="#/Dashboard">
                        <i className="fa fa-balance-scale"></i>
                        <p className="hidden-lg hidden-md">Attorney Insight</p>
                    </NavItem>
                    <NavItem eventKey={3} href="#">
                        {/* <i className="fa fa-search"></i> */}
                        <p className="hidden-lg hidden-md">Search</p>
                        <Autosuggest
                            suggestions={suggestions}
                            onSuggestionsFetchRequested={this.onSuggestionsFetchRequested}
                            onSuggestionsClearRequested={this.onSuggestionsClearRequested}
                            getSuggestionValue={getSuggestionValue}
                            onSuggestionSelected={this.onSuggestionSelected}  //. <-----

                            renderSuggestion={renderSuggestion}
                            inputProps={inputProps}
                            onSuggestionSelected={() => {
                                window.location.reload();
                            }}
                        />
                    </NavItem>
                </Nav>
                <Nav pullRight>
                    {/* <NavItem eventKey={1} href="#">Account</NavItem> */}
                    <NavDropdown eventKey={2} title="Support" id="basic-nav-dropdown-right">
                        <MenuItem eventKey={2.1}>Action</MenuItem>
                        <MenuItem eventKey={2.2}>Service</MenuItem>
                        <MenuItem eventKey={2.3}>Legal Team</MenuItem>
                        <MenuItem eventKey={2.4}>Tech Team</MenuItem>
                        <MenuItem eventKey={2.5}>Software Support</MenuItem>
                        <MenuItem divider />
                        <MenuItem eventKey={2.5}>Liberty Mutual</MenuItem>
                    </NavDropdown>
                </Nav>
            </div>
        );
    }
}

export default HeaderLinks;
