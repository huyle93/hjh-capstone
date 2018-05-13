import Dashboard from 'views/Dashboard/Dashboard';
import UserProfile from 'views/UserProfile/UserProfile';
import Icons from 'views/Icons/Icons';
import Notifications from 'views/Notifications/Notifications';

const appRoutes = [
    { path: "/dashboard", name: "Attorney Insight", icon: "pe-7s-graph", component: Dashboard },
    { path: "/user", name: "User Profile", icon: "pe-7s-user", component: UserProfile },
    { path: "/icons", name: "Icons", icon: "pe-7s-science", component: Icons },
    { path: "/notifications", name: "Notifications", icon: "pe-7s-bell", component: Notifications },
    { redirect: true, path:"/", to:"/dashboard", name: "Dashboard" }
];

export default appRoutes;
