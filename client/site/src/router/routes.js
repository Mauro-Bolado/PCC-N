const routes = [
  {
    path: "/",
    component: () => import("layouts/MainLayout.vue"),
    children: [
      { path: "/", component: () => import("pages/LoginPage.vue") },
      { path: "/militant", component: () => import("pages/MilitantsPage.vue") },
      { path: "/debt", component: () => import("pages/DebtPage.vue") },
      { path: "/core", component: () => import("pages/CorePage.vue") },
      { path: "/addcore", component: () => import("pages/AddCorePage.vue") },
    ],
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: "/:catchAll(.*)*",
    component: () => import("pages/ErrorNotFound.vue"),
  },
];

export default routes;
